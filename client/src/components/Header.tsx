import { useState } from 'react';
import { Button } from '@/components/ui/button';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
  DropdownMenuSeparator,
} from '@/components/ui/dropdown-menu';

export default function Header() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="sticky top-0 z-50 w-full border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 items-center justify-between">
        {/* Logo */}
        <div className="flex items-center gap-2">
          <div className="text-2xl font-bold text-primary">Autonova</div>
          <p className="text-xs text-muted-foreground hidden sm:block">KI. Echte Ergebnisse.</p>
        </div>

        {/* Navigation */}
        <nav className="hidden md:flex items-center gap-1">
          <Button variant="ghost" size="sm">
            Home
          </Button>

          {/* Leistungen Dropdown */}
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="ghost" size="sm">
                Leistungen ▼
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="start" className="w-56">
              <div className="px-2 py-1.5">
                <p className="text-xs font-semibold text-muted-foreground uppercase">SaaS-Produkte</p>
              </div>
              <DropdownMenuItem>Marketing & SEO</DropdownMenuItem>
              <DropdownMenuItem>Operations & Automation</DropdownMenuItem>
              <DropdownMenuItem>Data & Analytics</DropdownMenuItem>
              <DropdownMenuItem>Compliance & Legal</DropdownMenuItem>
              <DropdownMenuSeparator />
              <div className="px-2 py-1.5">
                <p className="text-xs font-semibold text-muted-foreground uppercase">Individuelle Lösungen</p>
              </div>
              <DropdownMenuItem>Dokumentenverarbeitung</DropdownMenuItem>
              <DropdownMenuItem>Predictive Maintenance</DropdownMenuItem>
              <DropdownMenuItem>Content-Automatisierung</DropdownMenuItem>
              <DropdownMenuSeparator />
              <div className="px-2 py-1.5">
                <p className="text-xs font-semibold text-muted-foreground uppercase">Freelancer-Services</p>
              </div>
              <DropdownMenuItem>SEO Audit</DropdownMenuItem>
              <DropdownMenuItem>Content Automation</DropdownMenuItem>
              <DropdownMenuItem>YouTube Recycling</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>

          <Button variant="ghost" size="sm">
            Über Uns
          </Button>
          <Button variant="ghost" size="sm">
            Preise
          </Button>
          <Button variant="ghost" size="sm">
            Blog
          </Button>
        </nav>

        {/* CTA Button */}
        <div className="flex items-center gap-4">
          <Button size="sm" className="hidden sm:inline-flex">
            Kontakt
          </Button>
        </div>
      </div>
    </header>
  );
}
