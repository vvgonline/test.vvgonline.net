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

```md
VVG.online.WEB.Test.PWA/
├── .github/
│ └── workflows/
│ └── deploy.yml
├── VVG.online.WEB.Test.PWA.csproj
├── Program.cs
├── App.razor
├── appsettings.json
├── wwwroot/
│ ├── index.html
│ ├── css/
│ │ ├── bootstrap.min.css (v5.3) Use CDN
│ │ └── app.scss (custom styles with golden ratio)
│ ├── js/
│ │ ├── interop.js (language translation, scroll, WhatsApp)
│ │ └── service-worker.js (PWA)
│ ├── data/
│ │ ├── services.json (metadata for 10 services)
│ │ ├── blog-posts.json (blog metadata)
│ │ └── facts-figures.json (statistics for charts)
│ ├── manifest.json (PWA manifest)
│ ├── icons/ (SVG icons)
│ └── favicon.ico
├── Pages/
│ ├── Home.razor
│ ├── Services.razor
│ ├── Blog.razor
│ ├── BlogPost.razor
│ ├── Contact.razor
│ ├── Presentations.razor
│ └── NotFound.razor
├── Components/
│ ├── Header.razor
│ ├── Footer.razor
│ ├── HeroBanner.razor (animated, 100vh)
│ ├── ServiceCard.razor
│ ├── BlogCard.razor
│ ├── MetaTags.razor (SEO, OpenGraph, JSON-LD)
│ ├── CookieConsent.razor
│ ├── Preloader.razor
│ ├── ScrollToTop.razor
│ ├── WhatsAppButton.razor
│ ├── LanguageToggle.razor
│ ├── Chart.razor (for data visualization)
│ └── LazyImage.razor
└── Models/
├── Service.cs
├── BlogPost.cs
├── Statistics.cs
└── SEOData.cs
```

```mermaid

Notes: example static data files have been added to the project under VVG.online.WEB.Test.PWA/wwwroot/data (services.json, blog-posts.json, facts-figures.json) so you can iterate on pages using this local static DB.
graph TD
    A[Project Root] --> B[Pages]
    A --> C[Components]
    A --> D[Models]
    A --> E[wwwroot]
    A --> F[Properties]
    A --> G[.github/workflows]

    B --> B1[Home.razor]
    B --> B2[Services.razor]
    B --> B3[Blog.razor]
    B --> B4[BlogPost.razor]
    B --> B5[Contact.razor]
    B --> B6[Presentations.razor]
    B --> B7[NotFound.razor]

    C --> C1[Header.razor]
    C --> C2[Footer.razor]
    C --> C3[HeroBanner.razor]
    C --> C4[ServiceCard.razor]
    C --> C5[BlogCard.razor]
    C --> C6[MetaTags.razor]
    C --> C7[CookieConsent.razor]
    C --> C8[Preloader.razor]
    C --> C9[ScrollToTop.razor]
    C --> C10[WhatsAppButton.razor]
    C --> C11[LanguageToggle.razor]
    C --> C12[Chart.razor]
    C --> C13[LazyImage.razor]

    D --> D1[Service.cs]
    D --> D2[BlogPost.cs]
    D --> D3[Statistics.cs]
    D --> D4[SEOData.cs]

    E --> E1[css]
    E --> E2[js]
    E --> E3[data]
    E --> E4[icons]
    E --> E5[manifest.json]
    E --> E6[favicon.ico]

    E1 --> E11[app.scss]
    E1 --> E12[bootstrap.css]

    E2 --> E21[interop.js]
    E2 --> E22[service-worker.js]

    E3 --> E31[services.json]
    E3 --> E32[blog-posts.json]
    E3 --> E33[facts-figures.json]

    F --> F1[launchSettings.json]

    G --> G1[deploy.yml]
```

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

- .NET 8 SDK or higher
- Visual Studio 2022 or VS Code
- Git

### Create Project

```bash
dotnet new blazorwasm -n VVG.online.WEB.Test.PWA --pwa
cd VVG.online.WEB.Test.PWA
```

### Add NuGet Packages

```bash
dotnet add package Microsoft.AspNetCore.Components.WebAssembly
dotnet add package System.Net.Http.Json
```

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

- [x] Meta tags (title, description, keywords)
- [x] OpenGraph tags for social sharing
- [x] Twitter Card metadata
- [x] JSON-LD structured data
- [x] Canonical URLs
- [x] Mobile-responsive design
- [x] Fast page load (critical CSS)
- [x] Sitemap (future)
- [x] Robots.txt (future)
- [x] Alt text for all images
- [x] Semantic HTML

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

**Next Steps:**

1. Review this structure
2. Confirm all requirements are met
3. Proceed with file-by-file implementation
