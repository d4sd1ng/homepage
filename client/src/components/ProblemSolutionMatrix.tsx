export default function ProblemSolutionMatrix() {
  const problems = [
    {
      problem: "Ineffiziente Prozesse",
      symptoms: "Mitarbeiter verbringen Stunden mit repetitiven Aufgaben",
      solution: "Prozessautomatisierung",
      benefit: "Bis zu 80% Zeitersparnis",
    },
    {
      problem: "Verlorenes Datenpotenzial",
      symptoms: "Unmengen an Daten werden nicht analysiert",
      solution: "Datenanalyse & Prognose",
      benefit: "30-50% bessere Vorhersagegenauigkeit",
    },
    {
      problem: "Schwache Online-Sichtbarkeit",
      symptoms: "Hohe Marketing-Kosten bei wenig qualifizierten Leads",
      solution: "Marketing-Automatisierung",
      benefit: "300% mehr organischer Traffic",
    },
    {
      problem: "Manuelle Dokumentenverarbeitung",
      symptoms: "Rechnungen und Verträge werden manuell erfasst",
      solution: "Dokumentenautomatisierung",
      benefit: "90% weniger manuelle Arbeit",
    },
  ];

  return (
    <section className="py-20 bg-background">
      <div className="container">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            Ihre Herausforderungen. Unsere KI-Lösungen.
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Entdecken Sie, wie künstliche Intelligenz Ihr Unternehmen transformieren kann
          </p>
        </div>

        <div className="grid gap-6">
          {problems.map((item, index) => (
            <div key={index} className="bg-card border border-border rounded-lg p-8 hover:border-primary/50 transition-colors">
              <div className="grid md:grid-cols-4 gap-6">
                <div>
                  <h3 className="font-bold text-lg text-primary mb-2">{item.problem}</h3>
                  <p className="text-sm text-muted-foreground">{item.symptoms}</p>
                </div>
                <div className="flex items-center justify-center">
                  <div className="text-2xl">→</div>
                </div>
                <div>
                  <h4 className="font-semibold text-accent mb-2">{item.solution}</h4>
                  <p className="text-sm text-muted-foreground">KI-gestützte Lösung</p>
                </div>
                <div>
                  <p className="font-bold text-lg text-green-500">{item.benefit}</p>
                  <p className="text-xs text-muted-foreground">Messbare Ergebnisse</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
