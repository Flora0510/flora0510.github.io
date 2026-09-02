---
layout: default
title: Contact
permalink: /contact/
---
<div class="wrap" style="padding: 3rem 0; max-width: 760px;">
  <h1>Contact</h1>
  <p>Une question, une réservation d'animation, une demande média ? Écris-nous.</p>

  <form class="contact" action="{{ site.contact_form_action }}" method="POST">
    <div>
      <label for="name">Nom</label>
      <input type="text" id="name" name="name" required>
    </div>
    <div>
      <label for="email">Courriel</label>
      <input type="email" id="email" name="email" required>
    </div>
    <div>
      <label for="message">Message</label>
      <textarea id="message" name="message" rows="6" required></textarea>
    </div>
    <button class="btn" type="submit">Envoyer</button>
  </form>

  <p style="margin-top: 2rem;">Tu peux aussi écrire directement à <a href="mailto:{{ site.email }}">{{ site.email }}</a>.</p>
</div>
