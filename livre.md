---
layout: default
title: Livres
permalink: /livres/
---
<div class="wrap" style="padding: 3rem 0;">
  <h1>Livres disponibles</h1>
  <p>Voici les livres que vous pouvez vous procurer.</p>

  <div class="shelf" style="margin-top: 2rem;">
    {% for livre in site.livres %}
    <a class="book" href="{{ livre.url | relative_url }}">
      <div class="book-cover">
        <img src="{{ livre.image | relative_url }}" alt="Couverture de {{ livre.title }}">
      </div>
      <h3>{{ livre.title }}</h3>
    </a>
    {% endfor %}
  </div>
</div>
