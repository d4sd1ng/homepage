import { Button } from "@/components/ui/button";

export default function CTASection() {
  return (
    <section className="py-20 bg-gradient-to-r from-primary/20 to-accent/20 border-t border-border">
      <div className="container">
        <div className="max-w-3xl mx-auto text-center space-y-8">
          <h2 className="text-4xl md:text-5xl font-bold">
            Bereit für die KI-Transformation?
          </h2>

          <p className="text-xl text-muted-foreground">
            Lassen Sie uns gemeinsam das Potenzial Ihrer Daten und Prozesse freisetzen. 
            Eine kostenlose Potenzial-Analyse zeigt Ihnen, wo die größten Chancen liegen.
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" className="text-base px-8">
              Kostenlose Potenzial-Analyse buchen
            </Button>
            <Button size="lg" variant="outline" className="text-base px-8">
              Kontakt aufnehmen
            </Button>
          </div>

          <div className="pt-8 border-t border-border">
            <p className="text-sm text-muted-foreground mb-4">
              Oder schreiben Sie mir direkt:
            </p>
            <p className="text-lg font-semibold">
              <a href="mailto:kontakt@autonova.ai" className="text-primary hover:underline">
                kontakt@autonova.ai
              </a>
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}
