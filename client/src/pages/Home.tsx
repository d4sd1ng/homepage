import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';

export default function Home() {
  const [activeTab, setActiveTab] = useState('home');
  const [industryFilter, setIndustryFilter] = useState('all');

  const industries = [
    { id: 'manufacturing', name: 'Industrie & Fertigung', icon: '🏭' },
    { id: 'finance', name: 'Finanzwesen', icon: '💰' },
    { id: 'marketing', name: 'Marketing & E-Commerce', icon: '🛍️' },
    { id: 'healthcare', name: 'Gesundheitswesen', icon: '⚕️' },
    { id: 'logistics', name: 'Logistik & Transport', icon: '🚚' },
    { id: 'education', name: 'Bildung', icon: '📚' },
  ];

  return (
    <div className="min-h-screen bg-background text-foreground">
      {/* Tab Navigation */}
      <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
        <TabsList className="w-full rounded-none border-b border-border bg-background sticky top-0 z-40 h-auto p-0 justify-start overflow-x-auto">
          <TabsTrigger value="home" className="rounded-none">Home</TabsTrigger>
          <TabsTrigger value="matrix" className="rounded-none">Problem-Lösung</TabsTrigger>
          <TabsTrigger value="services" className="rounded-none">Leistungen</TabsTrigger>
          <TabsTrigger value="industries" className="rounded-none">Branchen</TabsTrigger>
          <TabsTrigger value="whitepapers" className="rounded-none">Whitepapers</TabsTrigger>
          <TabsTrigger value="cases" className="rounded-none">Case Studies</TabsTrigger>
          <TabsTrigger value="podcasts" className="rounded-none">Podcasts</TabsTrigger>
          <TabsTrigger value="pricing" className="rounded-none">Preise</TabsTrigger>
          <TabsTrigger value="faq" className="rounded-none">FAQ</TabsTrigger>
          <TabsTrigger value="about" className="rounded-none">Über Uns</TabsTrigger>
        </TabsList>

        {/* HOME TAB */}
        <TabsContent value="home" className="m-0">
          <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
            {/* Hero Background with Overlay */}
            <div className="absolute inset-0 bg-gradient-to-br from-black via-black to-primary/20"></div>
            <div className="absolute top-0 left-1/4 w-96 h-96 bg-primary/10 rounded-full blur-3xl"></div>
            <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-secondary/10 rounded-full blur-3xl"></div>
            
            <div className="container relative z-10 max-w-4xl mx-auto text-center space-y-8 py-20">
              <h1 className="text-6xl md:text-7xl font-bold leading-tight">
                Künstliche Intelligenz.<br />
                <span className="text-secondary">Echte Ergebnisse.</span>
              </h1>
              
              <p className="text-lg md:text-xl text-muted-foreground font-medium">
                ✨ Seit 35 Jahren an der Spitze der Technologie – von BASIC auf dem C64 bis zu autonomen KI-Agenten.
              </p>
              
              <p className="text-xl md:text-2xl text-foreground max-w-3xl mx-auto leading-relaxed">
                Ich entwickle KI-Agenten, smarte Prozesse und maßgeschneiderte Automatisierungslösungen für Ihr Unternehmen.
              </p>
              
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 py-8 border-y border-border">
                <div><p className="text-2xl font-bold text-primary">35+</p><p className="text-sm text-muted-foreground">Jahre</p></div>
                <div><p className="text-2xl font-bold text-secondary">100%</p><p className="text-sm text-muted-foreground">Automatisiert</p></div>
                <div><p className="text-2xl font-bold text-accent">99.9%</p><p className="text-sm text-muted-foreground">Genauigkeit</p></div>
                <div><p className="text-2xl font-bold text-primary">24/7</p><p className="text-sm text-muted-foreground">Verfügbar</p></div>
              </div>
              
              <div className="flex flex-col sm:flex-row gap-4 justify-center pt-8">
                <button className="btn-primary">Kostenlose Potenzial-Analyse buchen</button>
                <button className="btn-outline">Unsere KI-Lösungen entdecken</button>
              </div>
            </div>
          </section>
        </TabsContent>

        {/* PROBLEM-SOLUTION MATRIX TAB */}
        <TabsContent value="matrix" className="m-0">
          <section className="section">
            <div className="container">
              <h2 className="text-center mb-4">Ihre Herausforderungen.</h2>
              <h3 className="text-center mb-12">Unsere KI-Lösungen.</h3>
              
              <div className="space-y-6">
                {[
                  { problem: 'Ineffiziente Prozesse', solution: 'Prozessautomatisierung', benefit: 'Bis zu 80% Zeitersparnis' },
                  { problem: 'Verlorenes Datenpotenzial', solution: 'Datenanalyse & Prognose', benefit: '30-50% bessere Vorhersagen' },
                  { problem: 'Schwache Online-Sichtbarkeit', solution: 'Marketing-Automatisierung', benefit: '300% mehr organischer Traffic' },
                  { problem: 'Manuelle Dokumentenverarbeitung', solution: 'Dokumentenautomatisierung', benefit: '90% weniger manuelle Arbeit' },
                ].map((item, i) => (
                  <Card key={i} className="card-dark accent-border">
                    <div className="grid md:grid-cols-3 gap-8">
                      <div>
                        <h4 className="text-primary mb-2">Problem</h4>
                        <p>{item.problem}</p>
                      </div>
                      <div>
                        <h4 className="text-secondary mb-2">Lösung</h4>
                        <p>{item.solution}</p>
                      </div>
                      <div>
                        <h4 className="text-accent mb-2">Vorteil</h4>
                        <p>{item.benefit}</p>
                      </div>
                    </div>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* SERVICES TAB */}
        <TabsContent value="services" className="m-0">
          <section className="section">
            <div className="container">
              <h2 className="text-center mb-4">Unsere KI-Lösungen</h2>
              <h3 className="text-center mb-12">für Ihren Erfolg</h3>
              
              <div className="grid md:grid-cols-2 gap-8">
                {[
                  { name: 'SEO Dominator', price: '49€/Monat', description: 'Google-Rankings automatisieren' },
                  { name: 'Prompt Optimizer', price: '19€/Monat', description: 'KI-Effizienz maximieren' },
                  { name: 'Bookwriter', price: '29€/Monat', description: 'Bücher schreiben lassen' },
                  { name: 'Web Scraping', price: '49€/Monat', description: 'Daten sammeln ohne Code' },
                ].map((service, i) => (
                  <Card key={i} className="card-dark">
                    <h4 className="text-primary mb-2">{service.name}</h4>
                    <p className="text-muted-foreground mb-4">{service.description}</p>
                    <p className="text-lg font-bold text-secondary mb-4">{service.price}</p>
                    <button className="btn-primary w-full">Mehr erfahren</button>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* INDUSTRIES TAB */}
        <TabsContent value="industries" className="m-0">
          <section className="section">
            <div className="container">
              <h2 className="text-center mb-4">Branchenspezifische</h2>
              <h3 className="text-center mb-12">Expertise</h3>
              
              <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                {industries.map((industry) => (
                  <Card key={industry.id} className="card-dark cursor-pointer" onClick={() => setIndustryFilter(industry.id)}>
                    <div className="text-4xl mb-4">{industry.icon}</div>
                    <h4 className="text-primary">{industry.name}</h4>
                    <p className="text-sm text-muted-foreground mt-2">Klicken für Case Studies, Whitepapers & Podcasts</p>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* WHITEPAPERS TAB */}
        <TabsContent value="whitepapers" className="m-0">
          <section className="section">
            <div className="container">
              <h2 className="text-center mb-4">Whitepapers &</h2>
              <h3 className="text-center mb-12">Lead-Magnete</h3>
              
              <div className="grid md:grid-cols-2 gap-8">
                {[
                  { id: 1, industry: 'manufacturing', title: 'Predictive Maintenance mit KI', description: 'Wie Sie Maschinenausfälle um 80% reduzieren' },
                  { id: 2, industry: 'finance', title: 'DSGVO & People Analytics', description: 'Rechtskonform KI in HR einsetzen' },
                  { id: 3, industry: 'marketing', title: 'SEO-Automatisierung 2025', description: 'Organischen Traffic 300% steigern' },
                ].filter(w => industryFilter === 'all' || w.industry === industryFilter).map((wp) => (
                  <Card key={wp.id} className="card-dark">
                    <h4 className="text-primary mb-2">{wp.title}</h4>
                    <p className="text-muted-foreground mb-4">{wp.description}</p>
                    <button className="btn-outline w-full">Kostenlos herunterladen</button>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* CASE STUDIES TAB */}
        <TabsContent value="cases" className="m-0">
          <section className="section">
            <div className="container">
              <h2 className="text-center mb-4">Erfolgs-</h2>
              <h3 className="text-center mb-12">geschichten</h3>
              
              <div className="space-y-8">
                {[
                  { id: 1, industry: 'manufacturing', company: 'Maschinenbauer (Mittelstand)', challenge: 'Ungeplante Ausfälle kosteten 50.000€/Monat', solution: 'Predictive Maintenance System', roi: '420%' },
                  { id: 2, industry: 'marketing', company: 'Online-Marketing-Agentur', challenge: 'Manuelle Content-Erstellung war teuer', solution: 'Vollautomatisierte Content-Pipeline', roi: '520%' },
                  { id: 3, industry: 'finance', company: 'Steuerberatungskanzlei', challenge: '30 Stunden/Woche manuelle Belegerfassung', solution: 'KI-gestützte Dokumentenverarbeitung', roi: '380%' },
                ].filter(c => industryFilter === 'all' || c.industry === industryFilter).map((cs) => (
                  <Card key={cs.id} className="card-dark accent-border">
                    <div className="grid md:grid-cols-2 gap-8">
                      <div>
                        <h4 className="text-primary mb-4">{cs.company}</h4>
                        <p className="text-muted-foreground mb-4"><strong>Challenge:</strong> {cs.challenge}</p>
                        <p className="text-muted-foreground"><strong>Lösung:</strong> {cs.solution}</p>
                      </div>
                      <div>
                        <p className="text-4xl font-bold text-secondary mb-4">{cs.roi}</p>
                        <p className="text-sm text-muted-foreground">ROI im ersten Jahr</p>
                      </div>
                    </div>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* PODCASTS TAB */}
        <TabsContent value="podcasts" className="m-0">
          <section className="section">
            <div className="container">
              <h2 className="text-center mb-4">Podcast-</h2>
              <h3 className="text-center mb-12">Episoden</h3>
              
              <div className="grid md:grid-cols-2 gap-8">
                {[
                  { id: 1, industry: 'manufacturing', title: 'KI in der Industrie 4.0', description: 'Interview mit Produktionsleiter', duration: '45 min' },
                  { id: 2, industry: 'marketing', title: 'Content-Automatisierung für Agenturen', description: 'Wie Sie 10x mehr Content produzieren', duration: '38 min' },
                  { id: 3, industry: 'finance', title: 'Trading Bots & KI', description: 'Automatisiertes Investieren', duration: '52 min' },
                ].filter(p => industryFilter === 'all' || p.industry === industryFilter).map((pod) => (
                  <Card key={pod.id} className="card-dark">
                    <h4 className="text-primary mb-2">{pod.title}</h4>
                    <p className="text-muted-foreground mb-4">{pod.description}</p>
                    <p className="text-sm text-secondary font-semibold mb-4">⏱ {pod.duration}</p>
                    <button className="btn-secondary w-full">Episode anhören</button>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* PRICING TAB */}
        <TabsContent value="pricing" className="m-0">
          <section className="section">
            <div className="container">
              <h2 className="text-center mb-4">Preise &</h2>
              <h3 className="text-center mb-12">Pakete</h3>
              
              <div className="grid md:grid-cols-2 gap-8">
                {[
                  { name: 'SEO Dominator', plans: ['49€/Monat', '99€/Monat', 'Enterprise'] },
                  { name: 'Prompt Optimizer', plans: ['Kostenlos', '19€/Monat', '49€/Monat'] },
                  { name: 'Dokumentenautomatisierung', plans: ['Ab 15.000€', '+ 297€/Monat'] },
                  { name: 'Predictive Maintenance', plans: ['Ab 25.000€', '+ 897€/Monat'] },
                ].map((item, i) => (
                  <Card key={i} className="card-dark">
                    <h4 className="text-primary mb-4">{item.name}</h4>
                    <div className="space-y-2 mb-6">
                      {item.plans.map((plan, j) => <p key={j} className="text-lg font-semibold text-secondary">{plan}</p>)}
                    </div>
                    <button className="btn-primary w-full">Jetzt starten</button>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* FAQ TAB */}
        <TabsContent value="faq" className="m-0">
          <section className="section">
            <div className="container max-w-3xl">
              <h2 className="text-center mb-4">Häufig gestellte</h2>
              <h3 className="text-center mb-12">Fragen</h3>
              
              <div className="space-y-6">
                {[
                  { q: 'Ist mein Unternehmen zu klein für KI?', a: 'Nein, gerade KMUs profitieren am meisten. Unsere Lösungen skalieren von 19€ bis Enterprise.' },
                  { q: 'Wie lange dauert die Implementierung?', a: 'SaaS-Tools: sofort. Individuelle Lösungen: 4-12 Wochen.' },
                  { q: 'Was passiert, wenn die KI Fehler macht?', a: 'Unsere Systeme haben >99% Genauigkeit mit Kontrollmechanismen.' },
                  { q: 'Ersetzen Sie meine Mitarbeiter?', a: 'Nein, wir machen sie produktiver. KI übernimmt repetitive Aufgaben.' },
                ].map((faq, i) => (
                  <Card key={i} className="card-dark">
                    <h4 className="text-primary mb-3">{faq.q}</h4>
                    <p className="text-muted-foreground">{faq.a}</p>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* ABOUT TAB */}
        <TabsContent value="about" className="m-0">
          <section className="section">
            <div className="container max-w-3xl">
              <h2 className="mb-12">35 Jahre Technologie-Expertise</h2>
              
              <div className="space-y-8">
                <p className="text-xl text-muted-foreground">
                  Mein Name ist [Name], und ich entwickle seit über drei Jahrzehnten digitale Lösungen – angefangen mit BASIC auf dem Commodore 64 bis hin zu den modernsten KI-Agenten von heute.
                </p>
                
                <div className="space-y-4">
                  <h3 className="text-2xl">Was mich auszeichnet:</h3>
                  
                  {[
                    { title: 'Technische Tiefe statt Oberflächlichkeit', desc: 'Ich entwickle maßgeschneiderte Lösungen von Grund auf, nicht nur bestehende Tools zusammenklicken.' },
                    { title: 'Bewährte Zuverlässigkeit', desc: 'Meine Systeme sind darauf ausgelegt, 24/7 zu laufen – ohne Ausfälle, ohne Überraschungen.' },
                    { title: 'Messbare Ergebnisse', desc: 'Jede Lösung ist darauf ausgelegt, konkrete, messbare Verbesserungen zu erzielen.' },
                  ].map((item, i) => (
                    <Card key={i} className="card-dark accent-border">
                      <h4 className="text-primary mb-2">{item.title}</h4>
                      <p className="text-muted-foreground">{item.desc}</p>
                    </Card>
                  ))}
                </div>
              </div>
            </div>
          </section>
        </TabsContent>
      </Tabs>
    </div>
  );
}
