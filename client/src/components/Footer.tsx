export default function Footer() {
  return (
    <footer className="bg-card border-t border-border py-12">
      <div className="container">
        <div className="grid md:grid-cols-4 gap-8 mb-8">
          <div>
            <h3 className="font-bold text-lg mb-4">Autonova</h3>
            <p className="text-sm text-muted-foreground">
              KI-Lösungen für echte Ergebnisse. Seit 35 Jahren.
            </p>
          </div>

          <div>
            <h4 className="font-semibold mb-4">Produkte</h4>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li><a href="#" className="hover:text-primary transition">SaaS-Tools</a></li>
              <li><a href="#" className="hover:text-primary transition">Individuelle Lösungen</a></li>
              <li><a href="#" className="hover:text-primary transition">Freelancer-Services</a></li>
            </ul>
          </div>

          <div>
            <h4 className="font-semibold mb-4">Unternehmen</h4>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li><a href="#" className="hover:text-primary transition">Über Uns</a></li>
              <li><a href="#" className="hover:text-primary transition">Blog</a></li>
              <li><a href="#" className="hover:text-primary transition">Kontakt</a></li>
            </ul>
          </div>

          <div>
            <h4 className="font-semibold mb-4">Rechtliches</h4>
            <ul className="space-y-2 text-sm text-muted-foreground">
              <li><a href="#" className="hover:text-primary transition">Impressum</a></li>
              <li><a href="#" className="hover:text-primary transition">Datenschutz</a></li>
              <li><a href="#" className="hover:text-primary transition">AGB</a></li>
            </ul>
          </div>
        </div>

        <div className="border-t border-border pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center gap-4">
            <p className="text-sm text-muted-foreground">
              © 2025 Autonova. Alle Rechte vorbehalten.
            </p>
            <div className="flex gap-6">
              <a href="#" className="text-muted-foreground hover:text-primary transition text-sm">
                LinkedIn
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition text-sm">
                Twitter
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition text-sm">
                GitHub
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
