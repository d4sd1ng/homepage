import { Button } from "@/components/ui/button";

export default function HeroSection() {
  return (
    <section className="min-h-screen flex items-center justify-center bg-gradient-to-br from-background via-background to-secondary/20 relative overflow-hidden">
      {/* Background decorative elements */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute top-20 left-10 w-72 h-72 bg-primary/10 rounded-full blur-3xl"></div>
        <div className="absolute bottom-20 right-10 w-96 h-96 bg-accent/10 rounded-full blur-3xl"></div>
      </div>

      <div className="container relative z-10">
        <div className="max-w-4xl mx-auto text-center space-y-8">
          {/* Main Headline */}
          <h1 className="text-5xl md:text-7xl font-bold leading-tight">
            Künstliche Intelligenz.
            <br />
            <span className="bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">
              Echte Ergebnisse.
            </span>
          </h1>

          {/* Subheadline */}
          <p className="text-xl md:text-2xl text-muted-foreground max-w-2xl mx-auto">
            Ich entwickle KI-Agenten, smarte Prozesse und maßgeschneiderte Automatisierungslösungen für Ihr Unternehmen.
          </p>

          {/* Experience Badge */}
          <div className="inline-block bg-card border border-border rounded-lg px-6 py-3">
            <p className="text-sm md:text-base font-semibold">
              ✨ Seit 35 Jahren an der Spitze der Technologie – von BASIC auf dem C64 bis zu autonomen KI-Agenten.
            </p>
          </div>

          {/* Trust Elements */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 py-8">
            <div className="text-center">
              <p className="text-sm font-semibold text-primary">35+ Jahre</p>
              <p className="text-xs text-muted-foreground">Erfahrung</p>
            </div>
            <div className="text-center">
              <p className="text-sm font-semibold text-primary">100%</p>
              <p className="text-xs text-muted-foreground">Automatisiert</p>
            </div>
            <div className="text-center">
              <p className="text-sm font-semibold text-primary">99.9%</p>
              <p className="text-xs text-muted-foreground">Genauigkeit</p>
            </div>
            <div className="text-center">
              <p className="text-sm font-semibold text-primary">24/7</p>
              <p className="text-xs text-muted-foreground">Verfügbar</p>
            </div>
          </div>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center pt-8">
            <Button size="lg" className="text-base px-8">
              Kostenlose Potenzial-Analyse buchen
            </Button>
            <Button size="lg" variant="outline" className="text-base px-8">
              Unsere KI-Lösungen entdecken
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
}
