---
layout: default
title: Accueil
---
<section class="hero">
  <div class="wrap">
    <h1>Des livres jeunesse à vivre autant qu'à lire</h1>
    <p>Deux autrices, des aventures pleines d'énigmes, et des animations pour donner le goût de lire aux jeunes lecteurs.</p>
    <p><a class="btn" href="{{ '/livres/' | relative_url }}">Découvrir les livres</a></p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="eyebrow-free-heading">Ce qu'on propose</h2>
    <div class="feature-grid">
      <div class="feature-card">
        <h3>Des romans d'aventure</h3>
        <p>Pirates, mystères et énigmes : des séries pensées pour donner envie de tourner la page.</p>
        <a href="{{ '/livres/' | relative_url }}">Voir les livres →</a>
      </div>
      <div class="feature-card">
        <h3>Animations scolaires</h3>
        <p>On visite les écoles et bibliothèques pour partager notre passion pour l'écriture.</p>
        <a href="{{ '/animations/' | relative_url }}">En savoir plus →</a>
      </div>
      <div class="feature-card">
        <h3>Parcours littéraire</h3>
        <p>Une façon ludique d'intégrer les arts numériques et la littérature en classe.</p>
        <a href="{{ '/parcours-litteraire/' | relative_url }}">En savoir plus →</a>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2 class="eyebrow-free-heading">Livres disponibles</h2>
    <div class="shelf">
      {% for livre in site.livres limit: 8 %}
      <a class="book" href="{{ livre.url | relative_url }}">
        <div class="book-cover">
          <img src="{{ livre.image | relative_url }}" alt="Couverture de {{ livre.title }}">
        </div>
        <h3>{{ livre.title }}</h3>
      </a>
      {% endfor %}
    </div>
    <p style="margin-top:1.5rem;"><a href="{{ '/livres/' | relative_url }}">Voir tous les livres →</a></p>
  </div>
</section>
