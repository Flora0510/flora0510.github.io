---
layout: default
title: Livres
permalink: /livres/
---
<div class="wrap" style="padding: 3rem 0;">
  <h1>Livres</h1>
  <p></p>

  {% if site.filtre_auteure %}
    {% assign livres_affiches = site.livres | where_exp: "livre", "livre.auteures contains site.filtre_auteure" %}
  {% else %}
    {% assign livres_affiches = site.livres %}
  {% endif %}

  {% assign ordre_ages = "Dès 3 ans,Dès 4 ans,Dès 5 ans,Dès 6 ans,Dès 7 ans,Dès 8 ans,Dès 9 ans,Dès 10 ans,Dès 11 ans,Dès 12 ans" | split: "," %}
  {% assign restants = livres_affiches %}

  {% for age_label in ordre_ages %}
    {% assign livres_de_cet_age = restants | where: "age", age_label %}
    {% if livres_de_cet_age.size > 0 %}
      <section style="margin-top: 2.5rem;">
        <h2>{{ age_label }}</h2>
        <div class="shelf" style="margin-top: 1.2rem;">
          {% for livre in livres_de_cet_age %}
          <a class="book" href="{{ livre.url | relative_url }}">
            <div class="book-cover{% if livre.format == 'carre' %} carre{% endif %}">
              <img src="{{ livre.image | relative_url }}" alt="Couverture de {{ livre.title }}">
            </div>
            <h3>{{ livre.title }}</h3>
          </a>
          {% endfor %}
        </div>
      </section>
      {% assign restants = restants | where_exp: "l", "l.age != age_label" %}
    {% endif %}
  {% endfor %}

  {% if restants.size > 0 %}
    <section style="margin-top: 2.5rem;">
      <h2>Autres</h2>
      <div class="shelf" style="margin-top: 1.2rem;">
        {% for livre in restants %}
        <a class="book" href="{{ livre.url | relative_url }}">
          <div class="book-cover{% if livre.format == 'carre' %} carre{% endif %}">
            <img src="{{ livre.image | relative_url }}" alt="Couverture de {{ livre.title }}">
          </div>
          <h3>{{ livre.title }}</h3>
        </a>
        {% endfor %}
      </div>
    </section>
  {% endif %}
</div>
