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

  OFFEN – die Preis-IDs fehlen noch
  ---------------------------------
  Fuer einen Checkout braucht Stripe die ID eines *Preises* (price_...), nicht
  die des Produkts (prod_...). Vorliegend sind bisher nur die Produkt-IDs.
  Solange price null ist, laesst sich fuer den jeweiligen Eintrag kein
  Checkout erzeugen.

  Wo die Werte stehen: Stripe-Dashboard, Produktkatalog, Produkt oeffnen, im
  Abschnitt Preise steht unter jedem Eintrag die price_...-ID. Dafuer wird
  weder ein API-Schluessel noch eine zweite Bestaetigung gebraucht.

  Zu klaeren ist ausserdem, ob die IDs aus dem Test- oder dem Livemodus
  stammen. Beide Modi fuehren getrennte Produkte und Preise; eine price-ID
  aus dem Livemodus funktioniert mit einem pk_test-Schluessel nicht.
*/
(function () {
  "use strict";

  window.NUROVELLE_STRIPE_PUBLISHABLE_KEY =
    "pk_test_51U9Z6jHhj2rcxrubmlRE4pxfwB4uw8PvFEurjDW6zwPn31Q5BA1S3kdzVTTcVpo6jl7EDrD8vE7RcAOrFiTEh1oT00n9lEhw83";

  window.NUROVELLE_STRIPE_MODE = "test";

  /*
    Zuordnung Produkt zu Preis.

    produkt    vorliegende prod_...-ID
    preis      die zugehoerige price_...-ID, sobald sie vorliegt
    bezeichnung  Klartext aus der Angabe des Auftraggebers

    Die Bezeichnungen stammen aus einer knappen Auflistung und sind noch zu
    bestaetigen, insbesondere bei den beiden Deep-Eintraegen: welcher der
    Aktionspreis bis 31.12.2026 ist und welcher der regulaere danach.
  */
  window.NUROVELLE_STRIPE_PRODUKTE = {
    bestehende_installation: {
      produkt: "prod_V9tUDrnbo63RZL",
      preis: null,
      bezeichnung: "Bestehende Installation",
    },
    deep_aktion: {
      produkt: "prod_V9tIUdRUIMyekB",
      preis: null,
      bezeichnung: "Deep-Potenzialanalyse, Aktionspreis bis 31.12.2026",
    },
    deep_regulaer: {
      produkt: "prod_V9tGguWrK1qqYb",
      preis: null,
      bezeichnung: "Deep-Potenzialanalyse, regulaer ab 01.01.2027",
    },
    betreuungspaket: {
      produkt: "prod_V9tPJda8QRbIm0",
      preis: null,
      bezeichnung: "Betreuungspaket",
    },
    buero: {
      produkt: "prod_V9tM4IZouHAJi7",
      preis: null,
      bezeichnung: "Buropaket",
    },
    handwerk: {
      produkt: "prod_V9tRhH5SL8Si27",
      preis: null,
      bezeichnung: "Handwerkspaket",
    },
    agency: {
      produkt: "prod_VBBusU1wAZMM28",
      preis: null,
      bezeichnung: "Agency",
    },
    pro_a: {
      produkt: "prod_VBBrkIeSiyEeeA",
      preis: null,
      bezeichnung: "ProA",
    },
  };
})();
