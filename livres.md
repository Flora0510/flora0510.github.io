---
layout: default
title: Livres
permalink: /livres/
---
<div class="wrap" style="padding: 3rem 0;">
  <h1>Livres disponibles</h1>
  <p>Voici nos livres.</p>

  <div class="shelf" style="margin-top: 2rem;">
    {% if site.filtre_auteure %}
      {% assign livres_affiches = site.livres | where_exp: "livre", "livre.auteures contains site.filtre_auteure" %}
      {% else %}
      {% assign livres_affiches = site.livres %}
      {% endif %}    
    {% for livre in livres_affiches %}
    <a class="book" href="{{ livre.url | relative_url }}">
      <div class="book-cover{% if livre.format == 'carre' %} carre{% endif %}">
        <img src="{{ livre.image | relative_url }}" alt="Couverture de {{ livre.title }}">
      </div>
      <h3>{{ livre.title }}</h3>
    </a>
    {% endfor %}
  </div>
</div>
