import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";

export default function FAQSection() {
  const faqs = [
    {
      question: "Wie lange dauert die Implementierung?",
      answer: "Das hängt von der Komplexität ab. SaaS-Tools sind sofort einsatzbereit. Maßgeschneiderte Lösungen dauern typischerweise 2-8 Wochen.",
    },
    {
      question: "Welche Daten brauchen Sie?",
      answer: "Wir benötigen Zugriff auf Ihre relevanten Datenquellen. Alle Daten werden DSGVO-konform verarbeitet und bleiben in Ihrer Kontrolle.",
    },
    {
      question: "Gibt es eine Testphase?",
      answer: "Ja! Die meisten SaaS-Tools haben kostenlose Testphasen oder kostenlose Pläne. Für maßgeschneiderte Lösungen bieten wir eine kostenlose Potenzial-Analyse an.",
    },
    {
      question: "Wie wird der ROI gemessen?",
      answer: "Wir definieren KPIs vor der Implementierung und liefern monatliche Reports. Der durchschnittliche ROI liegt bei 300-500% im ersten Jahr.",
    },
    {
      question: "Ist die Lösung skalierbar?",
      answer: "Absolut. Alle Systeme sind von Grund auf für Skalierbarkeit konzipiert. Sie wachsen mit Ihrem Unternehmen.",
    },
    {
      question: "Was ist mit Support und Wartung?",
      answer: "Wir bieten umfassenden Support und kontinuierliche Optimierung. Alle Systeme werden 24/7 überwacht.",
    },
  ];

  return (
    <section className="py-20 bg-secondary/50">
      <div className="container">
        <div className="max-w-3xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-4xl md:text-5xl font-bold mb-4">
              Häufig gestellte Fragen
            </h2>
            <p className="text-xl text-muted-foreground">
              Alles, was Sie über unsere KI-Lösungen wissen müssen
            </p>
          </div>

          <Accordion type="single" collapsible className="w-full">
            {faqs.map((faq, index) => (
              <AccordionItem key={index} value={`item-${index}`}>
                <AccordionTrigger className="text-lg font-semibold">
                  {faq.question}
                </AccordionTrigger>
                <AccordionContent className="text-base text-muted-foreground">
                  {faq.answer}
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </div>
      </div>
    </section>
  );
}
