from pathlib import Path

index_path = Path("homepage/index.html")
html = index_path.read_text(encoding="utf-8")

section_id = 'id="ki-projekt-start"'
css_marker = "/* Section 2: Der erste Schritt zu Ihrem KI-Projekt */"

css = r"""
/* Section 2: Der erste Schritt zu Ihrem KI-Projekt */
#ki-projekt-start {
  padding: 72px var(--side);
  background: #000000;
}

.ki-project-start-inner {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: minmax(0, 1.35fr) minmax(320px, .85fr);
  gap: 52px;
  align-items: center;
}

.ki-project-card-row {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  align-items: end;
}

.ki-project-card {
  position: relative;
  margin: 0;
  overflow: hidden;
  border: 2px solid #2E8B67;
  border-radius: 18px;
  background: #080B09;
  box-shadow: 0 18px 24px -18px #D4AF37E0;
}

.ki-project-card img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 1086 / 1448;
  object-fit: cover;
}

.ki-project-start-copy .kicker {
  margin-bottom: 8px;
}

.ki-project-start-copy .section-title {
  max-width: 580px;
}

.ki-project-start-copy .section-text {
  max-width: 620px;
}

.ki-project-start-copy .section-text p + p {
  margin-top: 14px;
}

.ki-project-start-copy .actions {
  margin-top: 28px;
}

@media (max-width: 1050px) {
  .ki-project-start-inner {
    grid-template-columns: 1fr;
    gap: 36px;
  }
}

@media (max-width: 680px) {
  #ki-projekt-start {
    padding: 56px 18px;
  }

  .ki-project-card-row {
    grid-template-columns: 1fr;
    gap: 18px;
  }

  .ki-project-card {
    max-width: 360px;
    margin: 0 auto;
  }
}
"""

section = r"""
<section class="section bg" id="ki-projekt-start">
  <div class="ki-project-start-inner">
    <div class="ki-project-card-row" aria-label="Drei Glaskarten zum Einstieg in ein KI-Projekt">
      <figure class="ki-project-card">
        <img src="assets/cards/glas2.png" alt="Schwarze Glaskarte mit grünem Rahmen"/>
      </figure>
      <figure class="ki-project-card">
        <img src="assets/cards/glas1.png" alt="Schwarze Glaskarte mit grünem Rahmen"/>
      </figure>
      <figure class="ki-project-card">
        <img src="assets/cards/glas3.png" alt="Schwarze Glaskarte mit grünem Rahmen"/>
      </figure>
    </div>

    <div class="ki-project-start-copy">
      <div class="kicker">Der erste Schritt</div>
      <h2 class="section-title">Der erste Schritt zu Ihrem <span class="gold">KI-Projekt</span></h2>
      <div class="section-text">
        <p>Ein KI-Projekt beginnt nicht mit der Auswahl eines Tools. Es beginnt mit der Frage, welcher Prozess verbessert, welche Daten nutzbar gemacht und welches Ergebnis erreicht werden soll.</p>
        <p>Nurovelle prüft, wo KI-Agenten, Automatisierung, Wissenssysteme oder individuelle Software tatsächlich Mehrwert schaffen. Dabei geht es nicht um allgemeine KI-Ideen, sondern um konkrete Geschäftsprozesse, technische Machbarkeit und eine realistische Umsetzung.</p>
        <p>So entsteht aus einer ersten Idee ein belastbarer nächster Schritt: vom Erstgespräch über die Potenzialanalyse bis zur Entwicklung eines Prototyps oder einer fertigen Lösung.</p>
      </div>
      <div class="actions">
        <a class="btn btn-primary" href="analyse.html">Kostenloses Erstgespräch vereinbaren</a>
      </div>
    </div>
  </div>
</section>
"""

if section_id not in html:
    if css_marker not in html:
        html = html.replace("</style>", css + "\n</style>", 1)

    hero_start = html.find('<section class="hero"')
    if hero_start == -1:
        raise RuntimeError("Hero section was not found.")
    hero_end = html.find("</section>", hero_start)
    if hero_end == -1:
        raise RuntimeError("Hero closing tag was not found.")
    hero_end += len("</section>")
    html = html[:hero_end] + "\n" + section + html[hero_end:]
    index_path.write_text(html, encoding="utf-8")

print("Sektion 2 wurde implementiert.")
