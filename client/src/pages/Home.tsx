import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card } from '@/components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { ChevronRight, Mail, Phone, MapPin, CheckCircle2, Zap, Shield, TrendingUp } from 'lucide-react';

export default function Home() {
  const [activeTab, setActiveTab] = useState('home');
  const [email, setEmail] = useState('');
  const [showLeadMagnet, setShowLeadMagnet] = useState(false);

  const services = [
    {
      category: 'SaaS - Priorität 1',
      items: [
        { name: 'Workflow Automation Engine', price: '€99-299/Mo', desc: 'KI-gestützte Prozessautomatisierung mit selbstlernenden Optimierungen' },
        { name: 'Multi-Platform Connector', price: '€99-299/Mo', desc: 'Echtzeit-Synchronisation zwischen allen deinen Systemen' },
        { name: 'HR Analytics Platform', price: '€99-299/Mo', desc: 'Predictive Analytics für bessere HR-Entscheidungen' },
      ]
    },
    {
      category: 'SaaS - Priorität 2',
      items: [
        { name: 'Invoice Processing Automation', price: '€99-299/Mo', desc: 'Automatische Rechnungsverarbeitung mit GoBD-Compliance' },
        { name: 'Quality Assurance Automation', price: '€99-299/Mo', desc: 'KI-gestützte Qualitätskontrolle mit 99%+ Genauigkeit' },
        { name: 'Content Calendar Automation', price: '€99-299/Mo', desc: '5-10x höhere Content-Produktion ohne extra Arbeit' },
      ]
    },
    {
      category: 'B2B Premium',
      items: [
        { name: 'Dokumentenverarbeitung', price: '€5.000-50.000', desc: 'Automatische Verarbeitung komplexer Geschäftsdokumente' },
        { name: 'Predictive Maintenance', price: '€5.000-50.000', desc: 'Vorhersage von Maschinenausfällen vor sie passieren' },
        { name: 'Customer Feedback Analysis', price: '€5.000-50.000', desc: 'KI-gestützte Analyse von Kundenfeedback' },
      ]
    },
    {
      category: 'Freelancer Services',
      items: [
        { name: 'SEO Audit & Optimierung', price: '€299-999', desc: '30-50% mehr organischer Traffic in 3 Monaten' },
        { name: 'Content Automation', price: '€299-999', desc: '4-8 SEO-optimierte Blog-Artikel pro Monat' },
        { name: 'YouTube Video Recycling', price: '€299-999', desc: 'Konvertiere Videos zu Shorts, TikToks, Reels' },
      ]
    }
  ];

  const industries = [
    { name: 'Fertigung & Industrie 4.0', icon: '🏭', description: 'Automatisierung von Produktionsprozessen, Qualitätskontrolle, Predictive Maintenance' },
    { name: 'Finanzdienstleistungen', icon: '💰', description: 'Rechnungsverarbeitung, Compliance, Risikomanagement, Fraud Detection' },
    { name: 'E-Commerce & Retail', icon: '🛍️', description: 'Inventory Management, Customer Analytics, Personalisierung, Logistics' },
    { name: 'Marketing & Agenturen', icon: '📢', description: 'Content Automation, Social Media Management, Lead Generation, Analytics' },
    { name: 'HR & Recruiting', icon: '👥', description: 'Talent Acquisition, Employee Analytics, Onboarding, Performance Management' },
    { name: 'Bildung & Akademie', icon: '🎓', description: 'Personalisiertes Lernen, Student Analytics, Automatisierte Bewertung' },
  ];

  const caseStudies = [
    {
      title: 'Von 3 Tagen auf 3 Stunden: Auftragsabwicklung 90% schneller',
      industry: 'Fertigung',
      result: '90% Zeitersparnis',
      description: 'Ein Mittelständler mit 100+ Aufträgen/Tag konnte seine Abwicklung von 3 Tagen auf 3 Stunden reduzieren durch Workflow Automation.'
    },
    {
      title: '300% mehr Reichweite mit dem gleichen Content-Budget',
      industry: 'Marketing',
      result: '300% Reichweite-Steigerung',
      description: 'Eine Agentur konnte ihre Content-Reichweite verdreifachen durch Content Repurposing und Multi-Channel-Automation.'
    },
    {
      title: '40% Reduktion der Fluktuation durch Predictive HR Analytics',
      industry: 'HR',
      result: '40% weniger Kündigungen',
      description: 'Ein großes Unternehmen konnte Kündigungen durch frühzeitige Identifikation von Flight-Risk-Mitarbeitern reduzieren.'
    }
  ];

  const whitepapers = [
    { title: 'DSGVO & People Analytics', industry: 'HR', downloadUrl: '#' },
    { title: 'GoBD & KI', industry: 'Finanzen', downloadUrl: '#' },
    { title: 'Unstrukturierte Daten in Gold verwandeln', industry: 'Data Science', downloadUrl: '#' },
  ];

  const podcasts = [
    { title: 'KI-Automatisierung in der Fertigung', industry: 'Industrie', duration: '45 min' },
    { title: 'Content Automation für Marketing-Teams', industry: 'Marketing', duration: '38 min' },
    { title: 'HR Analytics: Datengestützte Entscheidungen', industry: 'HR', duration: '52 min' },
  ];

  const faqs = [
    { q: 'Was ist Avataryx by TSc?', a: 'Avataryx by TSc ist ein KI-gestütztes Dienstleistungsunternehmen, das Unternehmen bei der Automatisierung ihrer Geschäftsprozesse hilft.' },
    { q: 'Für welche Branchen ist Avataryx by TSc geeignet?', a: 'Avataryx by TSc ist branchenübergreifend einsetzbar. Ich habe Erfahrung in Fertigung, Finanzdienstleistungen, E-Commerce, Marketing und vielen anderen Bereichen.' },
    { q: 'Wie lange dauert eine typische Implementierung?', a: 'Das hängt von der Komplexität ab. Einfache Automatisierungen: 2-4 Wochen. Mittlere Projekte: 1-3 Monate. SaaS-Produkte sind sofort einsatzbereit.' },
    { q: 'Wie sicher sind meine Daten?', a: 'Datensicherheit ist meine höchste Priorität. Alle Daten werden verschlüsselt übertragen und auf EU-gehosteten Servern gespeichert. DSGVO-konform.' },
    { q: 'Kann ich die SaaS-Produkte kostenlos testen?', a: 'Ja, alle SaaS-Produkte bieten eine kostenlose Trial-Phase (14-30 Tage). Sie können die volle Funktionalität testen, ohne eine Kreditkarte anzugeben.' },
  ];

  return (
    <div className="min-h-screen bg-black text-white">
      {/* Meta Tags */}
      <head>
        <title>Avataryx by TSc - KI-Automatisierung für dein Unternehmen</title>
        <meta name="description" content="Automatisiere deine Geschäftsprozesse mit KI. 35 Jahre Erfahrung, robuste Systeme, echte Ergebnisse." />
        <meta name="keywords" content="KI, Automatisierung, Workflow, SaaS, Industrie 4.0, Digitalisierung" />
        <meta property="og:title" content="Avataryx by TSc - Künstliche Intelligenz. Echte Ergebnisse." />
        <meta property="og:description" content="Automatisiere deine Geschäftsprozesse mit KI-gestützten Lösungen." />
        <meta property="og:image" content="https://avataryx.de/og-image.png" />
        <meta property="og:url" content="https://avataryx.de" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>

      {/* Navigation */}
      <nav className="sticky top-0 z-50 bg-black/95 backdrop-blur border-b border-blue-900/30">
        <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="text-2xl font-bold bg-gradient-to-r from-blue-500 to-green-500 bg-clip-text text-transparent">
            Avataryx by TSc
          </div>
          <Tabs value={activeTab} onValueChange={setActiveTab} className="hidden md:block">
            <TabsList className="bg-transparent border-b border-blue-900/30">
              <TabsTrigger value="home" className="text-sm">Home</TabsTrigger>
              <TabsTrigger value="problem" className="text-sm">Problem-Lösung</TabsTrigger>
              <TabsTrigger value="services" className="text-sm">Leistungen</TabsTrigger>
              <TabsTrigger value="industries" className="text-sm">Branchen</TabsTrigger>
              <TabsTrigger value="whitepapers" className="text-sm">Whitepapers</TabsTrigger>
              <TabsTrigger value="cases" className="text-sm">Case Studies</TabsTrigger>
              <TabsTrigger value="podcasts" className="text-sm">Podcasts</TabsTrigger>
              <TabsTrigger value="pricing" className="text-sm">Preise</TabsTrigger>
              <TabsTrigger value="faq" className="text-sm">FAQ</TabsTrigger>
              <TabsTrigger value="about" className="text-sm">Über Uns</TabsTrigger>
            </TabsList>
          </Tabs>
        </div>
      </nav>

      {/* Tab Content */}
      <Tabs value={activeTab} onValueChange={setActiveTab} className="w-full">
        {/* HOME TAB */}
        <TabsContent value="home" className="space-y-0">
          {/* Hero Section */}
          <section className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-950 via-black to-green-950 relative overflow-hidden">
            <div className="absolute inset-0 opacity-20">
              <div className="absolute top-20 left-10 w-72 h-72 bg-blue-500 rounded-full mix-blend-multiply filter blur-3xl"></div>
              <div className="absolute top-40 right-10 w-72 h-72 bg-green-500 rounded-full mix-blend-multiply filter blur-3xl"></div>
            </div>
            <div className="relative z-10 max-w-4xl mx-auto px-4 text-center">
              <h1 className="text-6xl md:text-7xl font-bold mb-6">
                <span className="text-blue-400">Künstliche Intelligenz.</span>
                <br />
                <span className="text-green-400">Echte Ergebnisse.</span>
              </h1>
              <p className="text-xl text-gray-300 mb-4">✨ Seit 35 Jahren an der Spitze der Technologie – von BASIC auf dem C64 bis zu modernen KI-Systemen.</p>
              <p className="text-lg text-gray-400 mb-8">Ich entwickle KI-Agenten, smarte Prozesse und maßgeschneiderte Automatisierungslösungen für Ihr Unternehmen.</p>
              <div className="flex gap-4 justify-center mb-12">
                <Button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-6 text-lg">
                  Kostenlose Potenzial-Analyse <ChevronRight className="ml-2" />
                </Button>
                <Button variant="outline" className="border-green-500 text-green-400 hover:bg-green-500/10 px-8 py-6 text-lg">
                  Mehr erfahren
                </Button>
              </div>
              <div className="grid grid-cols-4 gap-4 text-center">
                <div><div className="text-3xl font-bold text-blue-400">35+</div><div className="text-sm text-gray-400">Jahre Erfahrung</div></div>
                <div><div className="text-3xl font-bold text-green-400">100%</div><div className="text-sm text-gray-400">Automatisiert</div></div>
                <div><div className="text-3xl font-bold text-orange-400">99.9%</div><div className="text-sm text-gray-400">Genauigkeit</div></div>
                <div><div className="text-3xl font-bold text-purple-400">24/7</div><div className="text-sm text-gray-400">Verfügbar</div></div>
              </div>
            </div>
          </section>
        </TabsContent>

        {/* PROBLEM-LÖSUNG TAB */}
        <TabsContent value="problem" className="space-y-0">
          <section className="py-20 px-4 bg-black">
            <div className="max-w-6xl mx-auto">
              <h2 className="text-5xl font-bold text-green-400 mb-12 text-center">Deine Herausforderungen. Meine Lösungen.</h2>
              <div className="grid md:grid-cols-2 gap-8">
                {[
                  { problem: 'Manuelle Prozesse kosten Zeit & Geld', solution: 'Automatisierung spart 70-90% der Zeit' },
                  { problem: 'Datensilo zwischen Systemen', solution: 'Echtzeit-Synchronisation über alle Tools' },
                  { problem: 'Hohe Fehlerquoten bei Dateneingabe', solution: 'KI-gestützte Validierung mit <1% Fehlerquote' },
                  { problem: 'Schwierig, Daten zu verstehen', solution: 'Predictive Analytics für bessere Entscheidungen' },
                  { problem: 'Content-Produktion ist teuer', solution: '5-10x höhere Produktion mit KI' },
                  { problem: 'Keine Skalierbarkeit ohne mehr Personal', solution: 'Skaliere ohne Personalkosten zu verdoppeln' },
                ].map((item, i) => (
                  <Card key={i} className="bg-gradient-to-br from-blue-900/20 to-green-900/20 border-blue-500/30 p-6 hover:border-blue-500/60 transition">
                    <div className="flex gap-4">
                      <div className="text-3xl">❌</div>
                      <div>
                        <h3 className="text-lg font-bold text-red-400 mb-2">{item.problem}</h3>
                        <p className="text-gray-300">→ {item.solution}</p>
                      </div>
                    </div>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* SERVICES TAB */}
        <TabsContent value="services" className="space-y-0">
          <section className="py-20 px-4 bg-black">
            <div className="max-w-6xl mx-auto">
              <h2 className="text-5xl font-bold text-blue-400 mb-12 text-center">Meine Leistungen</h2>
              <div className="space-y-12">
                {services.map((category, i) => (
                  <div key={i}>
                    <h3 className="text-2xl font-bold text-orange-400 mb-6">{category.category}</h3>
                    <div className="grid md:grid-cols-3 gap-6">
                      {category.items.map((item, j) => (
                        <Card key={j} className="bg-gradient-to-br from-blue-900/30 to-green-900/30 border-blue-500/30 p-6 hover:border-blue-500/60 transition hover:shadow-lg hover:shadow-blue-500/20">
                          <h4 className="text-lg font-bold text-white mb-2">{item.name}</h4>
                          <p className="text-green-400 font-semibold mb-3">{item.price}</p>
                          <p className="text-gray-300 text-sm">{item.desc}</p>
                          <Button className="mt-4 w-full bg-blue-600 hover:bg-blue-700">Mehr erfahren</Button>
                        </Card>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* INDUSTRIES TAB */}
        <TabsContent value="industries" className="space-y-0">
          <section className="py-20 px-4 bg-black">
            <div className="max-w-6xl mx-auto">
              <h2 className="text-5xl font-bold text-green-400 mb-12 text-center">Branchen-Expertise</h2>
              <div className="grid md:grid-cols-2 gap-8">
                {industries.map((industry, i) => (
                  <Card key={i} className="bg-gradient-to-br from-blue-900/20 to-green-900/20 border-blue-500/30 p-8 hover:border-green-500/60 transition">
                    <div className="text-5xl mb-4">{industry.icon}</div>
                    <h3 className="text-xl font-bold text-white mb-3">{industry.name}</h3>
                    <p className="text-gray-300">{industry.description}</p>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* WHITEPAPERS TAB */}
        <TabsContent value="whitepapers" className="space-y-0">
          <section className="py-20 px-4 bg-black">
            <div className="max-w-6xl mx-auto">
              <h2 className="text-5xl font-bold text-blue-400 mb-12 text-center">Whitepapers & Lead-Magnete</h2>
              <div className="grid md:grid-cols-3 gap-8">
                {whitepapers.map((wp, i) => (
                  <Card key={i} className="bg-gradient-to-br from-blue-900/30 to-green-900/30 border-blue-500/30 p-8 hover:border-blue-500/60 transition">
                    <div className="text-4xl mb-4">📄</div>
                    <h3 className="text-lg font-bold text-white mb-2">{wp.title}</h3>
                    <p className="text-gray-400 text-sm mb-4">{wp.industry}</p>
                    <Button className="w-full bg-green-600 hover:bg-green-700" onClick={() => setShowLeadMagnet(true)}>
                      Kostenlos herunterladen
                    </Button>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* CASE STUDIES TAB */}
        <TabsContent value="cases" className="space-y-0">
          <section className="py-20 px-4 bg-black">
            <div className="max-w-6xl mx-auto">
              <h2 className="text-5xl font-bold text-green-400 mb-12 text-center">Erfolgsgeschichten</h2>
              <div className="grid md:grid-cols-3 gap-8">
                {caseStudies.map((cs, i) => (
                  <Card key={i} className="bg-gradient-to-br from-blue-900/30 to-green-900/30 border-green-500/30 p-8 hover:border-green-500/60 transition">
                    <div className="flex items-center justify-between mb-4">
                      <span className="text-sm font-semibold text-orange-400">{cs.industry}</span>
                      <CheckCircle2 className="text-green-400" />
                    </div>
                    <h3 className="text-lg font-bold text-white mb-3">{cs.title}</h3>
                    <p className="text-2xl font-bold text-green-400 mb-3">{cs.result}</p>
                    <p className="text-gray-300 text-sm">{cs.description}</p>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* PODCASTS TAB */}
        <TabsContent value="podcasts" className="space-y-0">
          <section className="py-20 px-4 bg-black">
            <div className="max-w-6xl mx-auto">
              <h2 className="text-5xl font-bold text-blue-400 mb-12 text-center">Podcast-Episoden</h2>
              <div className="grid md:grid-cols-3 gap-8">
                {podcasts.map((podcast, i) => (
                  <Card key={i} className="bg-gradient-to-br from-blue-900/30 to-green-900/30 border-blue-500/30 p-8 hover:border-blue-500/60 transition">
                    <div className="text-4xl mb-4">🎙️</div>
                    <h3 className="text-lg font-bold text-white mb-2">{podcast.title}</h3>
                    <p className="text-gray-400 text-sm mb-2">{podcast.industry}</p>
                    <p className="text-blue-400 text-sm font-semibold mb-4">⏱️ {podcast.duration}</p>
                    <Button className="w-full bg-blue-600 hover:bg-blue-700">Jetzt anhören</Button>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* PRICING TAB */}
        <TabsContent value="pricing" className="space-y-0">
          <section className="py-20 px-4 bg-black">
            <div className="max-w-6xl mx-auto">
              <h2 className="text-5xl font-bold text-green-400 mb-12 text-center">Preise & Pakete</h2>
              <div className="grid md:grid-cols-4 gap-6">
                {[
                  { name: 'SaaS Starter', price: '€99/Mo', features: ['Bis 10 Prozesse', 'Email Support', 'Basis-Integrationen'] },
                  { name: 'SaaS Professional', price: '€299/Mo', features: ['Bis 50 Prozesse', 'Priority Support', '50+ Integrationen'] },
                  { name: 'B2B Projekt', price: '€5.000+', features: ['Maßgeschneidert', 'Dedicated Support', 'Vollständige Integration'] },
                  { name: 'Freelancer Service', price: '€299-999', features: ['Low-Ticket Services', 'Flexible Pakete', 'Monatlich kündbar'] },
                ].map((plan, i) => (
                  <Card key={i} className="bg-gradient-to-br from-blue-900/30 to-green-900/30 border-blue-500/30 p-8 hover:border-blue-500/60 transition">
                    <h3 className="text-xl font-bold text-white mb-2">{plan.name}</h3>
                    <p className="text-3xl font-bold text-green-400 mb-6">{plan.price}</p>
                    <ul className="space-y-2 mb-6">
                      {plan.features.map((f, j) => (
                        <li key={j} className="text-gray-300 text-sm flex items-center">
                          <CheckCircle2 className="w-4 h-4 text-green-400 mr-2" /> {f}
                        </li>
                      ))}
                    </ul>
                    <Button className="w-full bg-blue-600 hover:bg-blue-700">Starten</Button>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* FAQ TAB */}
        <TabsContent value="faq" className="space-y-0">
          <section className="py-20 px-4 bg-black">
            <div className="max-w-4xl mx-auto">
              <h2 className="text-5xl font-bold text-blue-400 mb-12 text-center">Häufig gestellte Fragen</h2>
              <div className="space-y-4">
                {faqs.map((faq, i) => (
                  <Card key={i} className="bg-gradient-to-br from-blue-900/20 to-green-900/20 border-blue-500/30 p-6">
                    <h3 className="text-lg font-bold text-white mb-2">{faq.q}</h3>
                    <p className="text-gray-300">{faq.a}</p>
                  </Card>
                ))}
              </div>
            </div>
          </section>
        </TabsContent>

        {/* ABOUT TAB */}
        <TabsContent value="about" className="space-y-0">
          <section className="py-20 px-4 bg-gradient-to-br from-blue-950 via-black to-green-950">
            <div className="max-w-4xl mx-auto">
              <h2 className="text-5xl font-bold text-green-400 mb-8 text-center">Über Mich</h2>
              <Card className="bg-gradient-to-br from-blue-900/30 to-green-900/30 border-blue-500/30 p-8">
                <p className="text-gray-300 text-lg mb-6">
                  Ich bin Tino Schneider, ein erfahrener KI-Entwickler und Automation-Spezialist mit 35+ Jahren Erfahrung in der Softwareentwicklung. Meine Reise begann mit BASIC auf dem C64 und führte mich durch alle Phasen der Technologieentwicklung – von Desktop-Anwendungen über Web bis zu modernen KI-Systemen.
                </p>
                <p className="text-gray-300 text-lg mb-6">
                  Mit Avataryx by TSc möchte ich mein Wissen und meine Fähigkeiten mit Unternehmen teilen, die ihre Prozesse automatisieren und optimieren wollen. Mein Fokus liegt auf robusten, zuverlässigen Systemen – nicht auf Gimmicks oder Hype.
                </p>
                <p className="text-gray-300 text-lg">
                  Ich glaube an die Kraft von KI, wenn sie richtig eingesetzt wird: zur Automatisierung von Routineaufgaben, zur Verbesserung von Entscheidungen und zur Skalierung von Unternehmen ohne proportionale Kostensteigerung.
                </p>
              </Card>
            </div>
          </section>
        </TabsContent>
      </Tabs>

      {/* CTA Section */}
      <section className="py-20 px-4 bg-gradient-to-r from-blue-900 to-green-900">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl font-bold text-white mb-6">Bereit, dein Geschäft zu transformieren?</h2>
          <p className="text-xl text-gray-200 mb-8">Starte mit einer kostenlosen Potenzial-Analyse. Ich zeige dir, wie viel Zeit und Geld du mit Avataryx by TSc sparen kannst.</p>
          <Button className="bg-white text-blue-900 hover:bg-gray-100 px-8 py-6 text-lg font-bold" onClick={() => setShowLeadMagnet(true)}>
            Kostenlose Analyse anfordern
          </Button>
        </div>
      </section>

      {/* Lead Magnet Modal */}
      {showLeadMagnet && (
        <div className="fixed inset-0 bg-black/80 flex items-center justify-center z-50 p-4">
          <Card className="bg-gradient-to-br from-blue-900 to-green-900 border-blue-500 max-w-md w-full p-8">
            <h3 className="text-2xl font-bold text-white mb-4">Kostenlose Potenzial-Analyse</h3>
            <p className="text-gray-300 mb-6">Gib deine Email ein und erhalte sofort eine personalisierte Analyse, wie viel Zeit und Geld du sparen kannst.</p>
            <div className="space-y-4">
              <Input
                type="email"
                placeholder="deine@email.de"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="bg-black/50 border-blue-500/50 text-white placeholder-gray-500"
              />
              <Button className="w-full bg-green-600 hover:bg-green-700 text-white">
                Analyse erhalten
              </Button>
              <Button
                variant="ghost"
                className="w-full text-gray-400 hover:text-white"
                onClick={() => setShowLeadMagnet(false)}
              >
                Schließen
              </Button>
            </div>
          </Card>
        </div>
      )}

      {/* Footer */}
      <footer className="bg-black border-t border-blue-900/30 py-12 px-4">
        <div className="max-w-6xl mx-auto">
          <div className="grid md:grid-cols-4 gap-8 mb-8">
            <div>
              <h4 className="text-white font-bold mb-4">Avataryx by TSc</h4>
              <p className="text-gray-400 text-sm">KI-gestützte Automatisierung für dein Unternehmen.</p>
            </div>
            <div>
              <h4 className="text-white font-bold mb-4">Kontakt</h4>
              <div className="space-y-2 text-gray-400 text-sm">
                <p className="flex items-center gap-2"><MapPin className="w-4 h-4" /> Berliner Str. 12, 35039 Marburg</p>
                <p className="flex items-center gap-2"><Mail className="w-4 h-4" /> kontakt@avataryx.de</p>
                <p className="flex items-center gap-2"><Phone className="w-4 h-4" /> [Telefon folgt]</p>
              </div>
            </div>
            <div>
              <h4 className="text-white font-bold mb-4">Legal</h4>
              <div className="space-y-2 text-gray-400 text-sm">
                <p><a href="#" className="hover:text-blue-400">Impressum</a></p>
                <p><a href="#" className="hover:text-blue-400">Datenschutz</a></p>
                <p><a href="#" className="hover:text-blue-400">AGB</a></p>
              </div>
            </div>
            <div>
              <h4 className="text-white font-bold mb-4">Social</h4>
              <div className="space-y-2 text-gray-400 text-sm">
                <p><a href="#" className="hover:text-blue-400">LinkedIn</a></p>
                <p><a href="#" className="hover:text-blue-400">Twitter</a></p>
                <p><a href="#" className="hover:text-blue-400">YouTube</a></p>
              </div>
            </div>
          </div>
          <div className="border-t border-blue-900/30 pt-8 text-center text-gray-500 text-sm">
            <p>&copy; 2026 Avataryx by TSc by Tino Schneider. Alle Rechte vorbehalten.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
