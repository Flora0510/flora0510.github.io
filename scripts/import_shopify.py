#!/usr/bin/env python3
"""
Convertit un export CSV de produits Shopify en fiches livres Jekyll
(_livres/*.md), en téléchargeant les images de couverture.

Ne dépend que de la bibliothèque standard Python (aucune installation requise).

UTILISATION
-----------
1. Dans Shopify Admin > Produits, exporte un CSV :
   - soit "Tous les produits" pour tout importer d'un coup (sans collection),
   - soit filtre la liste par collection (barre de recherche :
     collection:nom-de-la-collection), sélectionne tout, puis "Exporter la
     sélection" — un CSV par collection te permet d'assigner le nom de série.

2. Lance le script pour un CSV qui regroupe des livres d'une même série :

     python3 scripts/import_shopify.py chemin/vers/export.csv --serie "Aventuriers des mers"

   Ou pour des livres hors série (indépendants) :

     python3 scripts/import_shopify.py chemin/vers/export.csv

3. Le script crée un fichier dans _livres/ par produit, télécharge l'image
   principale dans assets/images/livres/, et remplit le champ lien_achat
   avec ce que tu passes en --lien-achat (sinon un placeholder à corriger).

Relance le script pour chaque CSV/collection. Les fichiers existants ne sont
pas écrasés par défaut (utilise --forcer pour les remplacer).
"""

import argparse
import csv
import os
import re
import sys
import urllib.request
from html.parser import HTMLParser


class TexteSimpleHTML(HTMLParser):
    """Convertit grossièrement le Body (HTML) de Shopify en texte lisible."""

    BLOC = {"p", "div", "li", "br", "h1", "h2", "h3", "h4"}

    def __init__(self):
        super().__init__()
        self.morceaux = []

    def handle_starttag(self, tag, attrs):
        if tag == "li":
            self.morceaux.append("\n- ")
        elif tag in self.BLOC:
            self.morceaux.append("\n")

    def handle_endtag(self, tag):
        if tag in self.BLOC:
            self.morceaux.append("\n")

    def handle_data(self, data):
        self.morceaux.append(data)

    def texte(self):
        brut = "".join(self.morceaux)
        brut = re.sub(r"[ \t]+", " ", brut)
        brut = re.sub(r"\n{3,}", "\n\n", brut)
        return brut.strip()


def html_vers_texte(html):
    if not html:
        return ""
    parseur = TexteSimpleHTML()
    parseur.feed(html)
    return parseur.texte()


def slugifier(texte):
    texte = texte.lower().strip()
    texte = re.sub(r"[àâä]", "a", texte)
    texte = re.sub(r"[éèêë]", "e", texte)
    texte = re.sub(r"[îï]", "i", texte)
    texte = re.sub(r"[ôö]", "o", texte)
    texte = re.sub(r"[ùûü]", "u", texte)
    texte = re.sub(r"[ç]", "c", texte)
    texte = re.sub(r"[^a-z0-9]+", "-", texte)
    return texte.strip("-")


def echapper_yaml(valeur):
    return valeur.replace('"', '\\"')


def regrouper_par_produit(chemin_csv):
    """Regroupe les lignes du CSV Shopify par Handle (= un produit)."""
    produits = {}
    ordre = []
    with open(chemin_csv, newline="", encoding="utf-8-sig") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            handle = ligne.get("Handle", "").strip()
            if not handle:
                continue
            if handle not in produits:
                produits[handle] = {
                    "titre": "",
                    "corps_html": "",
                    "images": [],
                }
                ordre.append(handle)

            p = produits[handle]
            if ligne.get("Title", "").strip():
                p["titre"] = ligne["Title"].strip()
            if ligne.get("Body (HTML)", "").strip() and not p["corps_html"]:
                p["corps_html"] = ligne["Body (HTML)"]
            src = ligne.get("Image Src", "").strip()
            pos = ligne.get("Image Position", "").strip()
            if src:
                p["images"].append((pos or "999", src))

    for handle in ordre:
        produits[handle]["images"].sort(key=lambda t: t[0])

    return [(h, produits[h]) for h in ordre]


def telecharger_image(url, destination):
    if os.path.exists(destination):
        return
    try:
        urllib.request.urlretrieve(url, destination)
        print(f"  image téléchargée -> {destination}")
    except Exception as e:
        print(f"  ATTENTION: échec du téléchargement de l'image ({e})."
              f" Ajoute-la manuellement dans {destination}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", help="Chemin vers le CSV exporté de Shopify")
    ap.add_argument("--serie", default="", help="Nom de la série/collection à assigner à tous les livres de ce CSV")
    ap.add_argument("--lien-achat", default="", help="URL de point de vente par défaut (à corriger manuellement sinon)")
    ap.add_argument("--racine", default=".", help="Racine du projet Jekyll (défaut: dossier courant)")
    ap.add_argument("--forcer", action="store_true", help="Écrase les fiches livres existantes")
    args = ap.parse_args()

    dossier_livres = os.path.join(args.racine, "_livres")
    dossier_images = os.path.join(args.racine, "assets", "images", "livres")
    os.makedirs(dossier_livres, exist_ok=True)
    os.makedirs(dossier_images, exist_ok=True)

    produits = regrouper_par_produit(args.csv)
    if not produits:
        print("Aucun produit trouvé dans ce CSV.")
        sys.exit(1)

    for handle, p in produits:
        titre = p["titre"] or handle
        slug = slugifier(handle)
        chemin_fiche = os.path.join(dossier_livres, f"{slug}.md")

        if os.path.exists(chemin_fiche) and not args.forcer:
            print(f"- {titre}: fiche déjà existante, ignorée (--forcer pour écraser)")
            continue

        # Image principale
        chemin_image_relatif = f"/assets/images/livres/{slug}.jpg"
        if p["images"]:
            _, url_image = p["images"][0]
            ext = os.path.splitext(url_image.split("?")[0])[1] or ".jpg"
            chemin_image_relatif = f"/assets/images/livres/{slug}{ext}"
            chemin_image_absolu = os.path.join(dossier_images, f"{slug}{ext}")
            telecharger_image(url_image, chemin_image_absolu)
        else:
            print(f"  ATTENTION: aucune image trouvée pour {titre}, à ajouter manuellement.")

        resume = html_vers_texte(p["corps_html"]) or "Résumé du livre à ajouter."
        lien_achat = args.lien_achat or "https://lien-vers-le-point-de-vente.com"

        contenu = "---\n"
        contenu += f'title: "{echapper_yaml(titre)}"\n'
        if args.serie:
            contenu += f'serie: "{echapper_yaml(args.serie)}"\n'
        contenu += f"image: {chemin_image_relatif}\n"
        contenu += f'lien_achat: "{lien_achat}"\n'
        contenu += "---\n"
        contenu += resume + "\n"

        with open(chemin_fiche, "w", encoding="utf-8") as f:
            f.write(contenu)

        print(f"- {titre}: fiche créée -> {chemin_fiche}")

    print(f"\n{len(produits)} produit(s) traité(s).")
    print("Vérifie chaque fiche dans _livres/ : résumé, lien d'achat et image.")


if __name__ == "__main__":
    main()
