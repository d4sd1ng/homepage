import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

export default function CaseStudies() {
  const caseStudies = [
    {
      company: 'E-Commerce Shop (Retail)',
      challenge: 'Hohe Retourenquote (28%) und manuelle Rechnungsverarbeitung',
      solution: 'Dokumentenautomatisierung + Predictive Analytics für Retourenerkennung',
      results: [
        'Retourenquote um 90% reduziert',
        'Rechnungsverarbeitung um 95% automatisiert',
        'Kostenersparnis: 150.000€/Jahr',
      ],
      roi: '450%',
      industry: 'E-Commerce',
    },
    {
      company: 'Maschinenbau-Unternehmen',
      challenge: 'Ungeplante Maschinenausfälle kosten 50.000€/Tag',
      solution: 'Predictive Maintenance mit IoT-Integration und KI-Analyse',
      results: [
        'Ausfallzeiten um 80% reduziert',
        'Wartungskosten um 35% gesenkt',
        'Produktivität um 45% erhöht',
      ],
      roi: '320%',
      industry: 'Industrie',
    },
    {
      company: 'Marketing-Agentur',
      challenge: 'Manuelle Content-Erstellung für 20+ Kunden',
      solution: 'Multimodal Super Agent für Content-Automatisierung und Verteilung',
      results: [
        '300% mehr Content pro Monat',
        'Bearbeitungszeit um 85% reduziert',
        'Klientenzufriedenheit um 40% gestiegen',
      ],
      roi: '520%',
      industry: 'Marketing',
    },
  ];

  return (
    <section className="py-20 bg-secondary/50">
      <div className="container">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            Erfolgsgeschichten
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Echte Unternehmen, echte Ergebnisse – mit unseren KI-Lösungen
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {caseStudies.map((study, index) => (
            <Card key={index} className="p-8 border-t-4 border-t-primary hover:shadow-lg transition-all">
              <div className="mb-6">
                <p className="text-sm font-semibold text-accent uppercase mb-2">{study.industry}</p>
                <h3 className="text-xl font-bold">{study.company}</h3>
              </div>

              <div className="space-y-6 mb-8">
                <div>
                  <p className="text-xs font-semibold text-muted-foreground uppercase mb-2">Herausforderung</p>
                  <p className="text-sm text-muted-foreground">{study.challenge}</p>
                </div>

                <div>
                  <p className="text-xs font-semibold text-muted-foreground uppercase mb-2">Lösung</p>
                  <p className="text-sm text-muted-foreground">{study.solution}</p>
                </div>

                <div>
                  <p className="text-xs font-semibold text-muted-foreground uppercase mb-2">Ergebnisse</p>
                  <ul className="space-y-1">
                    {study.results.map((result, i) => (
                      <li key={i} className="text-sm text-green-500 flex items-start gap-2">
                        <span>✓</span>
                        <span>{result}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>

              <div className="border-t border-border pt-6">
                <p className="text-2xl font-bold text-primary">{study.roi}</p>
                <p className="text-xs text-muted-foreground">ROI im ersten Jahr</p>
              </div>
            </Card>
          ))}
        </div>

        <div className="text-center mt-12">
          <Button size="lg" variant="outline">
            Alle Case Studies ansehen
          </Button>
        </div>
      </div>
    </section>
  );
}
