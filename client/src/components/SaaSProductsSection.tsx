import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { saasProducts, saasCategories } from '@/lib/saasProducts';

export default function SaaSProductsSection() {
  const [activeCategory, setActiveCategory] = useState('marketing');

  const filteredProducts = saasProducts.filter(p => p.category === activeCategory);

  return (
    <section className="py-20 bg-secondary/50">
      <div className="container">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            Unsere SaaS-Lösungen
          </h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            36 KI-gestützte Tools für jeden Bereich Ihres Unternehmens
          </p>
        </div>

        {/* Category Filter */}
        <div className="flex flex-wrap gap-3 justify-center mb-12">
          {saasCategories.map((category) => (
            <Button
              key={category.id}
              variant={activeCategory === category.id ? 'default' : 'outline'}
              onClick={() => setActiveCategory(category.id)}
              className="transition-all"
            >
              {category.icon} {category.name}
            </Button>
          ))}
        </div>

        {/* Products Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredProducts.map((product) => (
            <div
              key={product.id}
              className="bg-card border border-border rounded-lg p-6 hover:border-primary/50 transition-all hover:shadow-lg"
            >
              <h3 className="text-xl font-bold mb-2 text-primary">{product.name}</h3>
              <p className="text-sm font-semibold text-accent mb-3">{product.headline}</p>
              <p className="text-sm text-muted-foreground mb-4">{product.description}</p>

              <div className="space-y-4 mb-6">
                <div>
                  <p className="text-xs font-semibold text-muted-foreground uppercase mb-2">Features</p>
                  <ul className="text-xs space-y-1">
                    {product.features.slice(0, 3).map((feature, i) => (
                      <li key={i} className="text-muted-foreground">✓ {feature}</li>
                    ))}
                  </ul>
                </div>

                <div>
                  <p className="text-xs font-semibold text-muted-foreground uppercase mb-2">Ergebnisse</p>
                  <ul className="text-xs space-y-1">
                    {product.results.slice(0, 2).map((result, i) => (
                      <li key={i} className="text-green-500">⬆ {result}</li>
                    ))}
                  </ul>
                </div>
              </div>

              <div className="border-t border-border pt-4 space-y-3">
                <div>
                  <p className="text-xs text-muted-foreground">{product.pricing}</p>
                  <p className="text-xs text-accent font-semibold">{product.cta}</p>
                </div>
                <Button size="sm" className="w-full" variant="outline">
                  {product.ctaText}
                </Button>
              </div>
            </div>
          ))}
        </div>

        <div className="text-center mt-12">
          <Button size="lg" variant="outline">
            Alle 36 SaaS-Tools ansehen
          </Button>
        </div>
      </div>
    </section>
  );
}
