# test.vvgonline.net

Repo to test new features of [VVG ONLINE's](www.vvgonline.net) website

Project created: 01-12-2025

Project Context: VVG ONLINE is Digital Business Consulting company.

Digital Business Consulting is a service that helps organizations navigate the complex and rapidly evolving digital landscape. It involves analyzing an organization's current state, identifying areas for improvement, and developing strategies to achieve its digital goals. Here are some key aspects of digital business consulting:

1. Digital Strategy: Developing a comprehensive digital strategy that aligns with the organization's overall business
   objectives. This involves identifying target audiences, understanding their needs and preferences, and creating a
   roadmap for delivering digital experiences that meet those needs.
2. Customer Experience: Improving customer experience through digital channels such as websites, mobile apps, social
   media, and email. This involves understanding customer behavior, creating user-friendly interfaces, and providing
   personalized experiences.
3. Digital Transformation: Helping organizations transform their business models, processes, and culture to take
   advantage of digital technologies. This includes developing new revenue streams, improving operational efficiency, and
   leveraging data and analytics to make more informed decisions.
4. Innovation: Identifying and exploring new digital opportunities for growth, such as emerging technologies like AI,
   blockchain, and the Internet of Things (IoT). This involves developing innovative products and services and creating
   new business models that can disrupt traditional industries.
5. Digital Operations: Improving the efficiency and effectiveness of digital operations, such as website performance,
   application development, and data management. This involves optimizing digital systems, processes, and tools to
   improve overall digital maturity.
6. Change Management: Managing the cultural and organizational changes required to successfully implement digital
   strategies. This involves communicating effectively with stakeholders, building buy-in for digital initiatives, and
   creating a culture of innovation and experimentation.
7. Measurement and Evaluation: Developing metrics and benchmarks to measure the success of digital initiatives. This
   involves tracking key performance indicators (KPIs) such as website traffic, user engagement, and revenue growth, and
   making adjustments to improve results.
8. Security and Privacy: Ensuring the security and privacy of digital assets, such as customer data and intellectual
   property. This involves implementing robust security measures, such as encryption and access controls, and complying
   with relevant regulations and standards.
9. Cloud Computing: Utilizing cloud computing to provide scalable and flexible digital infrastructure. This involves
   selecting the right cloud platforms, configuring virtual environments, and managing data storage and processing.
10. Artificial Intelligence (AI): Implementing AI technologies such as machine learning, natural language processing,
    and computer vision to enhance digital capabilities and improve decision-making.

Overall, digital business consulting helps organizations navigate the complex and rapidly evolving digital landscape and achieve their business objectives through effective digital strategies, processes, and technologies.

Project goals:

- setup a Blazor WASM app with SEO optimization in mind, a dynamic head tag with keywords, description, Open Graph metadata, Twitter card, JSON-LD, and a blog.
- Design should be elegant, clean, minimal, and modern.
- App will be hosted it on GitHub Pages And, its' [url](test.vvgonline.net)

## Blazor WebAssembly PWA Project Structure

### Key Features

- Responsive Design

  - Mobile-first approach
  - Bootstrap 5.3 for responsive grid
  - CSS media queries for tablet/desktop
  - Responsive images with lazy loading
  - Design style: Elegant, clean, minimal and modern

- Golden Ratio Typography

  - Base font size: 16px (1em)
  - Heading scale: 1.618x multiplier
  - EB Garamond for headings
  - IBM Plex Sans for body text

- Theme Toggle

  - Light theme: #d9d9d9 background
  - Dark theme: #0f172a background
  - Accent color: #ffdd33 (golden)
  - Persisted in localStorage

- Animated 100vh Hero Banners

  - Full-screen hero sections on each page
  - Gradient overlays with accent color
  - Smooth scroll animation
  - SVG background patterns

- Blog with Search & Filter

  - Dynamic meta tags per page
  - OpenGraph tags for social sharing
  - Twitter Card metadata
  - JSON-LD structured data (Organization, Article, WebSite)
  - Canonical URLs

- PWA Features

  - Manifest.json with app details
  - Service Worker for offline capability
  - Install prompt on browsers
  - Add to home screen

- Lazy Loading

  - Images load on-demand
  - Scripts loaded asynchronously
  - Preloader shown during initial load
  - Intersection Observer API for lazy images

- Interactive Components

  - Scroll-to-top button with smooth scroll
  - WhatsApp chat button (+919893261959)
  - Language toggle (Google Translate API integration)
  - Cookie consent dialog
  - Charts/graphs for statistics

- Blazor Components (C# Only)
  - No TypeScript/JavaScript logic
  - Server-side rendering with client-side interop for minimal JS
  - Component composition for modularity
  - Parameters for dynamic content

## Installation & Setup

### Prerequisites

- .NET 8.0.405 SDK or higher
- Visual Studio 2022 or VS Code
- Git

## GitHub Pages Deployment

### CI/CD Workflow (.github/workflows/deploy.yml)

See separate deploy.yml file for GitHub Actions configuration.

### Deploy Steps

1. Commit and push to main branch
2. GitHub Actions automatically:
   - Builds Blazor WASM app
   - Generates optimized bundle
   - Deploys to gh-pages branch
3. App goes live at: `https://vvgonline.github.io/VVG.online.WEB.Test.PWA/`

### Configure Repository

1. Go to Settings > Pages
2. Source: GitHub Actions
3. Branch: gh-pages
4. Enable GitHub Pages

## Data Structure (JSON)

### services.json

```json
{
  "services": [
    {
      "id": 1,
      "title": "Digital Strategy",
      "description": "...",
      "icon": "strategy.svg",
      "details": "..."
    }
  ]
}
```

### blog-posts.json

```json
{
  "posts": [
    {
      "id": 1,
      "title": "...",
      "slug": "...",
      "author": "...",
      "date": "2025-11-28",
      "readTime": 8,
      "tags": ["ai", "transformation"],
      "excerpt": "...",
      "content": "...",
      "featuredImage": "blog-1.svg"
    }
  ]
}
```

### facts-figures.json

```json
{
  "statistics": [
    {
      "category": "Market Size",
      "value": "268.46",
      "unit": "billion USD",
      "year": 2025,
      "growth": "7.4%"
    }
  ]
}
```

## Styling with Golden Ratio

### Font Sizes

- H1: 2.618rem (42.7px)
- H2: 1.618rem (25.9px)
- H3: 1.414rem (22.6px)
- Body: 1rem (16px)
- Small: 0.618rem (9.9px)

### Spacing Scale

- Base unit: 8px
- Multiples: 8, 16, 24, 32, 52, 84...

### Layout

- Column width: 64px + 16px gutter
- Container max-width: 1200px
- Aspect ratios: 16:9, 4:3, 1:1

## Performance Optimization

- Tree-shaking: enabled
- Trimming: enabled
- GZip compression
- Image optimization with SVGs
- Lazy component loading
- Code splitting

## SEO Checklist

- [ ] Meta tags (title, description, keywords)
- [ ] OpenGraph tags for social sharing
- [ ] Twitter Card metadata
- [ ] JSON-LD structured data
- [ ] Canonical URLs
- [ ] Mobile-responsive design
- [ ] Fast page load (critical CSS)
- [ ] Sitemap (future)
- [ ] Robots.txt (future)
- [ ] Alt text for all images
- [ ] Semantic HTML

## Components Overview

### MetaTags.razor

Dynamically sets page-specific SEO metadata

### HeroBanner.razor

Full-screen animated hero with gradient overlay

### LazyImage.razor

Progressive image loading with blur-up effect

### CookieConsent.razor

GDPR-compliant cookie notice

### Preloader.razor

Loading animation during initial page load

### Chart.razor

Data visualization using Chart.js or similar

## Testing & Deployment

### Local Testing

```bash
dotnet run --configuration Release
```

### Build for Production

```bash
dotnet publish -c Release
```

### Test PWA

- Open DevTools > Application > Manifest
- Verify manifest.json loads correctly
- Check Service Worker registration
- Test offline functionality

## Browser Support

- Chrome/Edge: 90+
- Firefox: 88+
- Safari: 14+
- Mobile browsers: iOS 14+, Android 9+

---

© 2025 VVG ONLINE. All rights reserved.
