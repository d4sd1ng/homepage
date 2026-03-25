import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';

export default function PricingSection() {
  const pricingPlans = [
    {
      name: 'Freelancer Services',
      description: 'Für schnelle, messbare Ergebnisse',
      price: 'Ab 500€',
      period: 'pro Projekt',
      features: [
        'SEO Audit & Strategie',
        'Content Automation',
        'YouTube Recycling',
        'Low-Ticket Services',
        'Schnelle Umsetzung',
        'Transparente Preise',
      ],
      cta: 'Service buchen',
      highlight: false,
    },
    {
      name: 'SaaS-Produkte',
      description: 'Skalierbare Lösungen für alle Bereiche',
      price: 'Ab 99€',
      period: 'pro Monat',
      features: [
        '36 verschiedene Tools',
        'Kostenlose Testphase',
        'Flexible Skalierung',
        'API-Integration',
        '24/7 Support',
        'Monatlich kündbar',
      ],
      cta: 'Kostenlos testen',
      highlight: true,
    },
    {
      name: 'Individuelle Lösungen',
      description: 'Maßgeschneiderte KI-Systeme',
      price: 'Ab 3.000€',
      period: 'pro Monat',
      features: [
        'Vollständige Automatisierung',
        'Dedizierter Support',
        'Regelmäßige Optimierung',
        'ROI-Garantie',
        'Unbegrenzte Skalierung',
        'Custom Integrationen',
      ],
      cta: 'Beratung buchen',
      highlight: false,
    },
  ];

  return (
    <section className="py-20 bg-background">
      <div className="container">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            Transparente Preise
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Für jedes Budget und jede Anforderung die richtige Lösung
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {pricingPlans.map((plan, index) => (
            <Card
              key={index}
              className={`p-8 flex flex-col transition-all ${
                plan.highlight
                  ? 'border-2 border-primary shadow-lg scale-105'
                  : 'border border-border hover:border-primary/50'
              }`}
            >
              {plan.highlight && (
                <div className="bg-primary text-primary-foreground text-xs font-bold px-3 py-1 rounded-full inline-block mb-4 w-fit">
                  BELIEBT
                </div>
              )}

              <h3 className="text-2xl font-bold mb-2">{plan.name}</h3>
              <p className="text-muted-foreground text-sm mb-6">{plan.description}</p>

              <div className="mb-8">
                <span className="text-4xl font-bold">{plan.price}</span>
                <span className="text-muted-foreground ml-2">{plan.period}</span>
              </div>

              <ul className="space-y-3 mb-8 flex-1">
                {plan.features.map((feature, i) => (
                  <li key={i} className="text-sm text-muted-foreground flex items-start gap-3">
                    <span className="text-primary mt-1">✓</span>
                    <span>{feature}</span>
                  </li>
                ))}
              </ul>

              <Button
                size="lg"
                className="w-full"
                variant={plan.highlight ? 'default' : 'outline'}
              >
                {plan.cta}
              </Button>
            </Card>
          ))}
        </div>

        <div className="text-center mt-12">
          <p className="text-muted-foreground mb-4">
            Alle Pläne können jederzeit angepasst oder gekündigt werden.
          </p>
          <Button size="lg" variant="outline">
            Kostenlose Potenzial-Analyse buchen
          </Button>
        </div>
      </div>
    </section>
  );
}
