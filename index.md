---
layout: default
title: Accueil
---
<section class="hero">
  <div class="wrap">
    <h1>Des livres jeunesse à lire et à vivre</h1>
    <p>Deux autrices, des aventures pleines d'énigmes, et des animations pour donner le goût de lire aux jeunes!</p>
    <p><a class="btn" href="{{ '/livres/' | relative_url }}">Découvrir les livres</a></p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="eyebrow-free-heading">Ce qu'on propose</h2>
    <div class="feature-grid">
      <div class="feature-card">
        <h3>Bandits des mers</h3>
        <p>Lora Boisvert et Carolyn Chouinard te proposent une expérience immersive alliant littérature et réalité augmentée. Grâce à l’application Les Éditions AppLit, plonge au cœur de l’intrigue, observe les décors à 360 degrés et résous les énigmes!</p>
        <a href="{{ '/livres/' | relative_url }}">En savoir plus →</a>
      </div>
      <div class="feature-card">
        <h3>Animations scolaires</h3>
        <p>Carolyn et Lora visitent les écoles et bibliothèques pour partager leur passion pour l'écriture.</p>
        <a href="{{ '/animations/' | relative_url }}">En savoir plus →</a>
      </div>
      <div class="feature-card">
        <h3>Parcours littéraire</h3>
        <p>Une façon ludique d'intégrer les arts numériques et la littérature en classe ou en bibliothèque.</p>
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
        <div class="book-cover{% if livre.format == 'carre' %} carre{% endif %}">
          <img src="{{ livre.image | relative_url }}" alt="Couverture de {{ livre.title }}">
        </div>
        <h3>{{ livre.title }}</h3>
      </a>
      {% endfor %}
    </div>
    <p style="margin-top:1.5rem;"><a href="{{ '/livres/' | relative_url }}">Voir tous les livres →</a></p>
  </div>
</section>
