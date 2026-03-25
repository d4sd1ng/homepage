import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

export default function ServicesOverview() {
  const services = [
    {
      title: 'SaaS-Produkte',
      description: '36 KI-gestützte Tools für jeden Bereich Ihres Unternehmens',
      features: [
        'Marketing & SEO Automation',
        'Operations & Automation',
        'Data & Analytics',
        'Compliance & Legal',
      ],
      icon: '🚀',
      cta: 'Alle Tools entdecken',
    },
    {
      title: 'Individuelle Lösungen',
      description: 'Maßgeschneiderte KI-Agenten für Ihre spezifischen Herausforderungen',
      features: [
        'Dokumentenverarbeitung',
        'Predictive Maintenance',
        'Content-Automatisierung',
        'Trading Bot & Finanzanalyse',
      ],
      icon: '⚙️',
      cta: 'Beratung buchen',
    },
    {
      title: 'Freelancer-Services',
      description: 'Hochwertige Services für schnelle, messbare Ergebnisse',
      features: [
        'SEO Audit & Strategie',
        'Content Automation',
        'YouTube Recycling',
        'Low-Ticket Services',
      ],
      icon: '💼',
      cta: 'Service buchen',
    },
  ];

  return (
    <section className="py-20 bg-background">
      <div className="container">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            Unsere Leistungen
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Drei Wege, wie wir Ihr Unternehmen transformieren
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {services.map((service, index) => (
            <Card key={index} className="p-8 border-2 hover:border-primary/50 transition-all">
              <div className="text-4xl mb-4">{service.icon}</div>
              <h3 className="text-2xl font-bold mb-2">{service.title}</h3>
              <p className="text-muted-foreground mb-6">{service.description}</p>

              <div className="space-y-2 mb-8">
                {service.features.map((feature, i) => (
                  <div key={i} className="text-sm text-muted-foreground flex items-start gap-2">
                    <span className="text-primary mt-1">✓</span>
                    <span>{feature}</span>
                  </div>
                ))}
              </div>

              <Button className="w-full" variant="outline">
                {service.cta}
              </Button>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}
