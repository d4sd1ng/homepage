export default function AboutSection() {
  return (
    <section className="py-20 bg-background">
      <div className="container">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-bold mb-8">
            35 Jahre Expertise. Von C64 bis KI.
          </h2>

          <div className="space-y-6 text-lg text-muted-foreground">
            <p>
              Meine Reise begann auf dem Commodore 64 mit BASIC-Programmierung. Seitdem habe ich jede Welle der Technologie mitgestaltet – von DOS und Windows über das Internet bis zur modernen Cloud-Infrastruktur und künstlicher Intelligenz.
            </p>

            <p>
              Diese 35 Jahre Erfahrung bedeuten nicht nur theoretisches Wissen. Es bedeutet, dass ich die Lektionen aus Jahrzehnten von Erfolgen und Fehlschlägen in jedes Projekt bringe. Ich weiß, was funktioniert und was nicht. Ich baue robuste Systeme, keine Gimmicks.
            </p>

            <p>
              Heute nutze ich diese Expertise, um KI-Lösungen zu schaffen, die echte Probleme lösen. Nicht die neueste Technologie um ihrer selbst willen, sondern die beste Technologie für Ihre spezifische Herausforderung.
            </p>

            <p>
              Meine Multimodal Super Agents sind das Ergebnis dieser Erfahrung: vollautomatisierte Systeme, die Ihre Prozesse transformieren, Ihre Daten nutzen und Ihr Geschäft skalieren – ohne dass Sie ständig dahinter herlaufen müssen.
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8 mt-12 pt-12 border-t border-border">
            <div className="text-center">
              <p className="text-4xl font-bold text-primary mb-2">35+</p>
              <p className="text-muted-foreground">Jahre Erfahrung</p>
            </div>
            <div className="text-center">
              <p className="text-4xl font-bold text-accent mb-2">100+</p>
              <p className="text-muted-foreground">Projekte realisiert</p>
            </div>
            <div className="text-center">
              <p className="text-4xl font-bold text-green-500 mb-2">∞</p>
              <p className="text-muted-foreground">Leidenschaft für Code</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
