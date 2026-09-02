---
layout: default
title: Zone profs
permalink: /zone-profs/
---
<div class="wrap" style="padding: 3rem 0;">
  <h1>Zone profs</h1>
  <p>Des ressources pour préparer une visite en classe ou prolonger la lecture des livres.</p>

  <div class="ressource-list" style="margin-top: 2rem;">
    {% for item in site.ressources %}
    <div class="ressource-item">
      <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
      <p>{{ item.resume }}</p>
    </div>
    {% endfor %}
  </div>
</div>
