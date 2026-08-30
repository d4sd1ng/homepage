/*
  Nurovelle Homepage – Stripe-Konfiguration

  Diese Datei enthaelt ausschliesslich Konfigurationswerte. Sie enthaelt keine
  Bezahllogik, keinen Checkout und keinen Aufruf der Stripe-API.

  Einbindung (noch in keiner Seite gesetzt, siehe todo.md):

      <script src="stripe-config.js"></script>

  Die Datei muss vor dem Skript geladen werden, das die Werte liest. Gelesen
  wird nach der im Projekt bestehenden Konvention aus analyse.html:

      const key = window.NUROVELLE_STRIPE_PUBLISHABLE_KEY;

  Der Publishable Key ist oeffentlich. Stripe gibt ihn fuer den Einsatz im
  Browser aus; er steht in jeder Stripe-Integration im ausgelieferten
  Quelltext. Er erlaubt keine Kontoaenderungen und keine Abfrage von Daten.
  Der Secret Key (sk_...) darf niemals in dieser Datei oder in einer anderen
  Datei dieses Repositories stehen; er gehoert ausschliesslich auf den Server.

  Aktueller Stand: Testmodus. Es werden keine echten Zahlungen ausgeloest.
*/
(function () {
  "use strict";

  window.NUROVELLE_STRIPE_PUBLISHABLE_KEY =
    "pk_test_51U9Z6jHhj2rcxrubmlRE4pxfwB4uw8PvFEurjDW6zwPn31Q5BA1S3kdzVTTcVpo6jl7EDrD8vE7RcAOrFiTEh1oT00n9lEhw83";

  window.NUROVELLE_STRIPE_MODE = "test";
})();
