import { Card } from '@/components/ui/card';

export default function IndustryExpertise() {
  const industries = [
    {
      name: 'Industrie & Fertigung',
      icon: '🏭',
      solutions: ['Predictive Maintenance', 'Quality Assurance', 'Supply Chain Optimization'],
      description: 'Reduzieren Sie Ausfallzeiten um 80% und optimieren Sie Ihre Produktion',
    },
    {
      name: 'Finanzdienstleistungen',
      icon: '💰',
      solutions: ['Trading Bot', 'Risk Analysis', 'Compliance Automation'],
      description: 'Automatisieren Sie Risikomanagement und Compliance in Echtzeit',
    },
    {
      name: 'Marketing & E-Commerce',
      icon: '🛍️',
      solutions: ['SEO Automation', 'Content Marketing', 'Customer Journey Mapping'],
      description: 'Steigern Sie Ihre Conversion um 300% mit KI-gestütztem Marketing',
    },
    {
      name: 'Gesundheitswesen',
      icon: '⚕️',
      solutions: ['Data Analytics', 'Patient Management', 'Predictive Analytics'],
      description: 'Verbessern Sie Patientenergebnisse durch datengestützte Entscheidungen',
    },
    {
      name: 'Logistik & Transport',
      icon: '🚚',
      solutions: ['Route Optimization', 'Demand Forecasting', 'Fleet Management'],
      description: 'Optimieren Sie Ihre Logistik und sparen Sie bis zu 40% Kosten',
    },
    {
      name: 'Bildung & E-Learning',
      icon: '📚',
      solutions: ['Content Automation', 'Student Analytics', 'Personalized Learning'],
      description: 'Personalisieren Sie das Lernerlebnis für jeden Schüler',
    },
  ];

  return (
    <section className="py-20 bg-background">
      <div className="container">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            Branchenspezifische Expertise
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Lösungen für jede Industrie – mit bewährten Erfolgsmustern
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {industries.map((industry, index) => (
            <Card key={index} className="p-6 hover:border-primary/50 transition-all">
              <div className="text-4xl mb-4">{industry.icon}</div>
              <h3 className="text-xl font-bold mb-2">{industry.name}</h3>
              <p className="text-sm text-muted-foreground mb-4">{industry.description}</p>

              <div className="space-y-2">
                <p className="text-xs font-semibold text-muted-foreground uppercase">Unsere Lösungen</p>
                {industry.solutions.map((solution, i) => (
                  <div key={i} className="text-sm text-primary flex items-center gap-2">
                    <span>→</span>
                    <span>{solution}</span>
                  </div>
                ))}
              </div>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}
