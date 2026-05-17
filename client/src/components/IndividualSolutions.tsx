import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';

export default function IndividualSolutions() {
  const solutions = [
    {
      title: 'Dokumentenverarbeitung',
      description: 'Automatisierte Verarbeitung von Rechnungen, Verträgen und Dokumenten mit KI',
      benefits: ['90% weniger manuelle Arbeit', 'Fehlerquote < 1%', 'DSGVO-konform'],
      price: 'Ab 5.000€/Monat',
    },
    {
      title: 'Predictive Maintenance',
      description: 'Vorhersage von Maschinenausfällen bevor sie passieren',
      benefits: ['80% weniger Ausfallzeiten', 'Kostenersparnis bis 40%', 'Echtzeit-Monitoring'],
      price: 'Ab 8.000€/Monat',
    },
    {
      title: 'Content-Automatisierung',
      description: 'Vollautomatische Erstellung und Verteilung von Content über alle Kanäle',
      benefits: ['300% mehr Content', 'Konsistente Qualität', 'SEO-optimiert'],
      price: 'Ab 3.000€/Monat',
    },
    {
      title: 'Trading Bot & Finanzanalyse',
      description: 'KI-gestützte Handelsstrategien und Marktanalysen in Echtzeit',
      benefits: ['24/7 Automatisierung', 'Backtesting-validiert', 'Risikomanagement'],
      price: 'Ab 10.000€/Monat',
    },
  ];

  return (
    <section className="py-20 bg-secondary/50">
      <div className="container">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            Individuelle KI-Lösungen
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Maßgeschneiderte Systeme für Ihre spezifischen Herausforderungen
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          {solutions.map((solution, index) => (
            <Card key={index} className="p-8 border-l-4 border-l-primary hover:shadow-lg transition-all">
              <h3 className="text-2xl font-bold mb-2">{solution.title}</h3>
              <p className="text-muted-foreground mb-6">{solution.description}</p>

              <div className="space-y-2 mb-8">
                {solution.benefits.map((benefit, i) => (
                  <div key={i} className="text-sm text-muted-foreground flex items-center gap-2">
                    <span className="text-green-500">⬆</span>
                    <span>{benefit}</span>
                  </div>
                ))}
              </div>

              <div className="flex items-center justify-between pt-6 border-t border-border">
                <p className="font-semibold text-primary">{solution.price}</p>
                <Button size="sm" variant="outline">
                  Anfrage
                </Button>
              </div>
            </Card>
          ))}
        </div>

        <div className="text-center mt-12">
          <Button size="lg">
            Kostenlose Beratung buchen
          </Button>
        </div>
      </div>
    </section>
  );
}
