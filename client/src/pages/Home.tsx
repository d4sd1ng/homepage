import Header from "@/components/Header";
import HeroSection from "@/components/HeroSection";
import ProblemSolutionMatrix from "@/components/ProblemSolutionMatrix";
import ServicesOverview from "@/components/ServicesOverview";
import SaaSProductsSection from "@/components/SaaSProductsSection";
import IndividualSolutions from "@/components/IndividualSolutions";
import AboutSection from "@/components/AboutSection";
import IndustryExpertise from "@/components/IndustryExpertise";
import CaseStudies from "@/components/CaseStudies";
import PricingSection from "@/components/PricingSection";
import FAQSection from "@/components/FAQSection";
import CTASection from "@/components/CTASection";
import NewsletterSignup from "@/components/NewsletterSignup";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-1">
        <HeroSection />
        <ProblemSolutionMatrix />
        <ServicesOverview />
        <SaaSProductsSection />
        <IndividualSolutions />
        <AboutSection />
        <IndustryExpertise />
        <CaseStudies />
        <PricingSection />
        <FAQSection />
        <CTASection />
        <NewsletterSignup />
      </main>
      <Footer />
    </div>
  );
}
