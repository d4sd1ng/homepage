import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { useState } from 'react';

export default function NewsletterSignup() {
  const [email, setEmail] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: Integrate with email service (Mailchimp, ConvertKit, etc.)
    setIsSubmitted(true);
    setTimeout(() => {
      setEmail('');
      setIsSubmitted(false);
    }, 3000);
  };

  return (
    <section className="py-16 bg-gradient-to-r from-primary/10 to-accent/10 border-t border-border">
      <div className="container">
        <div className="max-w-2xl mx-auto text-center space-y-6">
          <h2 className="text-3xl md:text-4xl font-bold">
            Bleiben Sie auf dem Laufenden
          </h2>
          <p className="text-lg text-muted-foreground">
            Erhalten Sie wöchentliche Tipps zu KI-Automatisierung, Case Studies und exklusive Angebote direkt in Ihren Posteingang.
          </p>

          <form onSubmit={handleSubmit} className="flex gap-3 max-w-md mx-auto">
            <Input
              type="email"
              placeholder="Ihre E-Mail-Adresse"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="flex-1"
            />
            <Button type="submit" size="lg">
              Abonnieren
            </Button>
          </form>

          {isSubmitted && (
            <p className="text-sm text-green-500 font-semibold">
              ✓ Danke! Bitte bestätigen Sie Ihre E-Mail.
            </p>
          )}

          <p className="text-xs text-muted-foreground">
            Wir respektieren Ihre Privatsphäre. Abmeldung jederzeit möglich.
          </p>
        </div>
      </div>
    </section>
  );
}
