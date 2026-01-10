# specs/0_Project_Vision.md

```markdown
# 0_Project_Vision.md

## Project Goals

The primary goals for the `test.vvgonline.net` project are:

1. **Blazor WASM Application Setup:** Establish a Blazor WebAssembly (WASM) application.
2. **SEO Optimization:** Implement comprehensive SEO features, including:
    * Dynamic head tags.
    * Keywords, descriptions, Open Graph metadata, Twitter card, and JSON-LD.
    * A functional blog.
3. **Design Aesthetics:** Ensure an elegant, clean, minimal, and modern design.
4. **Hosting:** Deploy the application on GitHub Pages.
5. **Progressive Web App (PWA):** Integrate PWA features for enhanced user experience and offline capabilities.
6. **Performance:** Optimize for fast page load times.
7. **User Interaction:** Include interactive components for a richer user experience.
8. **Security:** Implement security measures such as HTTPS, Cross-Origin Resource Sharing (CORS), and Content Security Policy.
9. **Accessibility:** Ensure the application is accessible to all users, including those with disabilities.
10. **Localization:** Support multiple languages and regions.
11. **Analytics:** Integrate analytics tools like Google Analytics
12. **Documentation:** Provide comprehensive documentation for the codebase
13. **Code Quality:** Adhere to Blazor Component best practices (C# only).
14. **Testing:** Implement unit and integration tests to ensure application reliability.
15. **Continuous Integration/Continuous Deployment (CI/CD):** Set up CI/CD pipelines for automated testing and deployment.
16. **Community Engagement:** Foster a community around the project for feedback and contributions.

## Blog Experience Vision

The `test.vvgonline.net` blog should:

1. Serve as the canonical, markdown‑driven archive of VVG ONLINE thought leadership, with Git as the source of truth for all posts.
2. Provide a focused reading experience with:
   - A clean main reading column.
   - A contextual sidebar with about/profile, highlights, and navigation aids.
   - A collapsible “On this page” table of contents (TOC) for long posts.
3. Support efficient discovery of content through:
   - A dedicated archives page with year and tag filters.
   - A prominent search box for full‑text search across titles and content.
4. Support a markdown‑first authoring workflow:
   - Posts authored as markdown files with front‑matter (title, slug, date, tags, draft, excerpt).
   - A build step that generates a JSON index for fast client‑side rendering in Blazor WebAssembly.
5. Keep interaction intentionally minimal:
   - Simple share/copy‑link actions and clear CTAs (e.g., contact, services) instead of heavy commenting systems in the initial release.
6. Maintain performance and accessibility:
   - Static hosting (GitHub Pages) friendly architecture.
   - Sanitary markdown→HTML rendering to avoid XSS while preserving rich formatting.

The project aims to serve as a testbed for new features of VVG ONLINE's website.
```

# specs/1_Product_Requirements.md

```markdown
# 1_Product_Requirements.md

## Functional Requirements and Missing Implementations

This document outlines the specific product requirements and details the implementation steps needed to fulfill the project goals for `test.vvgonline.net`.

### 1. SEO Configuration Files

* **Requirement:** Create and populate the following JSON files within `src/wwwroot/data/` to provide default SEO metadata:
    * `metadata.json`: For general site-wide metadata.
    * `twitter-card.json`: For Twitter Card specific metadata.
    * `open-graph.json`: For Open Graph protocol metadata.
* **Purpose:** These files are critical for the `MetadataService.cs` to dynamically set meta tags for pages, ensuring proper social sharing and search engine visibility, as described in the README.
* **Example Structure (`metadata.json`):**

    ```json
    {
      "title": "VVG ONLINE - Digital Business Consulting",
      "description": "Leading digital business consulting services to transform your enterprise.",
      "keywords": "digital strategy, consulting, AI, transformation, business growth"
    }
    ```

* **Example Structure (`twitter-card.json`):**

    ```json
    {
      "card": "summary_large_image",
      "site": "@YourTwitterHandle",
      "creator": "@YourTwitterHandle"
    }
    ```

* **Example Structure (`open-graph.json`):**
    ```json
    {
      "type": "website",
      "url": "https://vvgonline.github.io/test.vvgonline.net/",
      "site_name": "VVG ONLINE"
    }
    ```
* **Example Structure (`json-ld.json`):**

    ```json
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "url": "https://vvgonline.github.io/test.vvgonline.net/",
      "name": "VVG ONLINE - Digital Business Consulting",
      "description": "Leading digital business consulting services to transform your enterprise.",
      "publisher": {
        "@type": "Organization",
        "name": "VVG ONLINE",
        "url": "https://vvgonline.net"
      },
      "potentialAction": {
        "@type": "SearchAction",
        "target": "https://vvgonline.github.io/test.vvgonline.net/archives?q={search_term_string}",
        "query-input": "required name=search_term_string"
      }
    }
    ```

* **Requirement:** Add a `json-ld.json` file under `src/wwwroot/data/` and ensure `MetadataService.cs` injects a `<script type="application/ld+json">` tag on pages where structured data is needed (site‑wide on Home, and optionally enriched on blog post pages).

### 2. Blog Search and Filtering

* **Requirement:** Implement search and filtering capabilities on the `Blog.razor` page.
* **Functionality:**
    * **Search:** Allow users to search blog posts by title, author, or excerpt content.
    * **Filtering:** Enable filtering of blog posts by tags.
    * **Dynamic Updates:** The displayed list of blog posts should update in real-time as the user types in the search bar or selects filters.
* **Data Source:** Utilize individual `blog-posts.md` markdown files as a data source for blog post data and 'metadata.json' for SEO metadata.
    * **UI Elements:** Include a search input field and a tag filter dropdown or checkbox list above the blog post listings.
    * **Performance:** Ensure efficient searching and filtering to maintain a responsive user experience, even with a large number of blog posts.
    * **Styling:** Ensure the search and filter UI elements align with the overall design aesthetics of the site.
    * **Scrap current blog posts from the existing blog section:** Extract existing blog posts from the current blog section of the site to populate the new blog structure.

### 2.1 Blog Content Model and Storage

* **Requirement:** Use markdown files with front‑matter as the single source of truth for blog posts.
* **Data Structure:**
  * Each post is a `.md` file stored under `wwwroot/blog/` (or `wwwroot/data/blog/`), with front‑matter keys:
    * `title` (string)
    * `slug` (string, URL path segment)
    * `publishedAt` (ISO date string)
    * `tags` (string array)
    * `excerpt` (string, optional)
    * `draft` (boolean)
* **Behavior:**
  * Draft posts are excluded from public listings and routing.
  * Slugs must be unique; navigating to `/blog/{slug}` loads the corresponding post.
* **Index Generation:**
  * A build step generates a `blog-index.json` file containing:
    * `title`, `slug`, `publishedAt`, `tags`, `excerpt`, `draft` (no full body content).
  * The Blazor WASM app loads `blog-index.json` to power listings, archives, and search.

### 2.2 Blog Layouts and Views

* **Requirement:** Separate general site layout from blog layout.
* **Main Layout (`MainLayout`):**
  * Used for non‑blog pages (home, services, contact).
  * Single‑column or simple top‑nav layout, without blog sidebar or TOC.
* **Blog Layout (`BlogLayout`):**
  * Used for `/blog`, `/archives`, and `/blog/{slug}` routes.
  * Two‑column layout on desktop:
    * Main column: post list or article content (approx. 65–70% width).
    * Sidebar: about/profile card, highlights, tags, and optional TOC.
  * On mobile, columns stack vertically (main content first, then sidebar modules).

* **Blog Index Page (`/blog`):**
  * Displays a vertical list of posts ordered by `publishedAt` (newest first).
  * Each list item includes:
    * Title (links to `/blog/{slug}`).
    * Published date.
    * Tags.
    * Excerpt (from front‑matter, or auto‑generated from content).
    * "Read more" link.
  * A slim filter bar above the list allows filtering by tag (single or multi‑select).

* **Single Post Page (`/blog/{slug}`):**
  * Shows title, date, and tags at the top.
  * Renders the markdown content as sanitized HTML.
  * End‑of‑post “More like this” area:
    * At least 3 related posts matching tags and/or year, if available.
  * End‑of‑post CTA area:
    * A configurable component for newsletter signup or contact/services.

### 2.3 Archives, Filters, and Search

* **Requirement:** Provide a dedicated archives view with year/tag filters and search.

* **Archives Page (`/archives`):**
  * A search box at the top that filters posts by title and content.
  * Year filter:
    * Filter by `publishedAt` year (e.g., 2023, 2024, 2025).
    * Year groupings are collapsible/expandable.
  * Tag filter:
    * Clickable tag chips or checkboxes.
    * Selecting multiple tags constrains results (logical AND).
  * Results area:
    * Shows posts grouped by year, respecting active filters and search query.

* **Search Behavior:**
  * Search is applied client‑side against a pre‑built index:
    * At minimum, `title`, `excerpt`, and lightweight content snippet fields.
  * Search and filters combine:
    * Search text AND year AND tags.
  * Clearing search and filters resets to all posts.

### 2.4 Sidebar and Table of Contents (TOC)

* **Requirement:** Provide a contextual sidebar with an optional collapsible TOC.

* **Sidebar Content:**
  * About/Profile card:
    * Short description and link to “About”/“Services”.
  * Highlights:
    * Configurable list of pinned posts or series.
  * Tag cloud or tag list:
    * Limited to a curated set of top tags for compactness.
  * Back to Top button:
    * Smoothly scrolls to the top of the page when clicked.
    * should be visible after scrolling down a certain distance.

* **TOC Behavior:**
  * The TOC is shown only on single post pages.
  * It is generated from the post’s heading structure (H2/H3).
  * A “Contents” or “On this page” header labels the TOC.
  * Collapsible:
    * Desktop: expanded by default.
    * Mobile: collapsed by default with a chevron or “Show contents” control.
  * Clicking a TOC item scrolls smoothly to the corresponding heading.
  * The currently visible section is highlighted (scrollspy‑style state).

### 2.5 Interaction and Sharing

* **Requirement:** Keep interaction minimal and focused on navigation and sharing.

* **Initial Interaction Features:**
  * A “Copy link” action on single posts (copies canonical URL to clipboard).
  * Optional light‑weight share button that triggers the browser’s native share dialog where supported.
  * Clear call‑to‑action at the end of posts (e.g., “Contact VVG ONLINE” or “Explore services”).

* **Deferred Features (Out of Scope for v1):**
  * Custom comment system.
  * Like counters or visible subscriber counts.
  * In‑browser blog post editing and publishing UI.


### 3. Theme Toggle

* **Requirement:** Implement a user-friendly mechanism to switch between the defined light and dark themes.
* **UI Element:** Integrate a visible toggle control (e.g., a button or switch) in a prominent location (e.g., header).
* **Persistence:** The user's selected theme preference must be saved using `localStorage` so it persists across sessions.
* **Styling:** Ensure theme changes correctly apply the specified color palettes and that the golden ratio typography and spacing scales are respected across both themes.

### 4. Animated Hero Banners

* **Requirement:** Verify and enhance the `HeroBanner.razor` component to ensure it meets the design specifications.
* **Animation:** Implement smooth scroll animations and visually appealing gradient overlays.
* **Dimensions:** Ensure hero banners occupy the full viewport height (100vh) and feature SVG background patterns as described.

### 5. Chart Implementation for Statistics

* **Requirement:** Integrate data visualization components using `Chart.razor`.
* **Data Integration:** Populate charts with statistical data sourced from `facts-figures.json`.
* **Placement:** Display these charts on relevant pages (e.g., Home or a dedicated statistics page if applicable) to visualize key figures.

### 6. PWA Offline Capabilities and Install Prompt

* **Requirement:** Ensure the Progressive Web App (PWA) functionality is fully realized.
* **Offline Capability:** Verify that the `service-worker.js` effectively caches application assets and allows users to access the site offline.
* **Install Prompt:** Confirm that the browser displays a prompt for users to install the PWA to their home screen.

### 7. Sitemap and Robots.txt Generation

* **Requirement:** Generate `sitemap.xml` dynamically using the `SitemapService.cs` and `robots.txt` files.
* **Purpose:** These files are essential for search engine optimization, guiding crawlers and providing a map of the site's structure.
* **Method:** Investigate and implement a mechanism for their generation, potentially through build-time processes or dedicated Blazor components/services.

### 8. Page-Specific SEO Metadata Verification

* **Requirement:** Confirm that individual pages can correctly utilize page-specific SEO metadata.
* **Verification:** Review key pages (e.g., Home, Services, Blog) to ensure the `MetadataService` is correctly injected and `SetPageMetadata` is called with unique and relevant data for title, description, keywords, and social sharing tags.
```

# specs/2_Architecture.md

```markdown
# 2_Architecture.md

## Project Architecture Overview

The `test.vvgonline.net` project is built as a Blazor WebAssembly (WASM) Progressive Web Application (PWA) using C#.

### Core Structure

*   **Blazor WASM:** The application runs entirely in the browser, leveraging WebAssembly for near-native performance. It utilizes .NET runtime compiled to WebAssembly.
*   **Project Structure:** Follows the standard Blazor WASM template, organized into:
    *   `src/`: Contains the main application code.
        *   `Pages/`: Razor components for different application pages (Home, Services, Blog, etc.).
        *   `Components/`: Reusable UI components (e.g., `MetaTags.razor`, `HeroBanner.razor`, `Chart.razor`).
        *   `Models/`: C# classes defining data structures (e.g., `Service.cs`, `BlogPost.cs`).
        *   `wwwroot/`: Static assets, including `index.html`, CSS, JS, images, and JSON data files.
            *   `data/`: Contains JSON files for services, statistics, and markdown files blog posts.
            *   `css/`: Stylesheets, including Bootstrap and custom `app.css`.
            *   `js/`: JavaScript files for interop and service workers.
    *   `.github/workflows/deploy.yml`: CI/CD pipeline for deployment to GitHub Pages.
    *   `specs/`: Directory for documentation (this file).
*   **SEO Implementation:** Handled via the `MetadataService.cs` and the `MetaTags.razor` component. Metadata is fetched from JSON files in `wwwroot/data/` and dynamically injected into the `<head>` of the HTML document.
*   **PWA Features:** Integrated via `manifest.json` and `service-worker.js` located in `wwwroot/`.

### Blog Content Storage and Indexing

* **Markdown Storage:**
  * Blog posts are stored as markdown files with front‑matter under `wwwroot/blog/` (or a `wwwroot/data/blog/` directory).
  * Front‑matter is parsed at build time by a script/tool to produce a `blog-index.json` file containing:
    * `title`, `slug`, `publishedAt`, `tags`, `excerpt`, `draft`.

* **Content Delivery in Blazor WASM:**
  * The Blazor WASM app reads `blog-index.json` at startup (or on first blog page load) to populate in‑memory models (`BlogPostSummary`).
  * For individual posts, the app:
    * Either fetches pre‑rendered, sanitized HTML from `wwwroot/blog/{slug}.html`; or
    * Fetches markdown from `wwwroot/blog/{slug}.md` and renders it via a markdown component with HTML sanitization.

* **Layouts:**
  * `MainLayout.razor`:
    * Houses shared shell elements for non‑blog pages (header, footer, basic navigation).
  * `BlogLayout.razor`:
    * Provides a two‑column grid (main + sidebar).
    * Used for routes under `/blog` and `/archives`.
    * Hosts the blog sidebar (about card, highlights, tags, TOC placeholder).

### Blog Search, Archives, and TOC Integration

* **Search and Filtering:**
  * The blog and archives pages consume `blog-index.json` to:
    * Filter posts by tags and year.
    * Perform client‑side search over a lightweight index structure (potentially a separate `blog-search-index.json`).
  * State for filters and search can be held in a scoped service (e.g., `BlogFilterStateService`) to synchronize components without excessive re‑renders.

* **Archives View:**
  * Implemented as `Archives.razor` and uses:
    * `BlogLayout.razor` for its shell.
    * The shared blog index for all filtering and grouping logic.

* **Table of Contents Component:**
  * A reusable `BlogToc.razor` component:
    * Accepts a collection of headings or parses the rendered content via JS interop.
    * Renders a nested list of links to sections (IDs based on slugified headings).
    * Integrates with a scrollspy mechanism (JS interop or a dedicated component) to highlight the active section.

* **Sidebar Composition:**
  * Sidebar is composed of modular components:
    * `BlogSidebarAbout.razor`
    * `BlogSidebarHighlights.razor`
    * `BlogSidebarTags.razor`
    * `BlogToc.razor`
  * Each component receives its data via parameters or shared services, maintaining separation of concerns.

### Integration of New Features

*   **SEO JSON Files:** New JSON files (`metadata.json`, `twitter-card.json`, `open-graph.json`) will be placed in `src/wwwroot/data/` and referenced by `MetadataService.cs`.
*   **Blog Search & Filter:** Logic will be added to `Blog.razor` to filter and search `blog-posts.json` data client-side.
*   **Theme Toggle:** A new component or logic within existing layout components will manage theme state (using `localStorage`) and apply CSS classes accordingly.
*   **Animated Hero Banners:** The existing `HeroBanner.razor` will be enhanced with CSS animations and potentially JavaScript interop for advanced effects.
*   **Charts:** The `Chart.razor` component will be implemented to consume data from `facts-figures.json` and render charts using a JavaScript charting library (e.g., Chart.js) via Blazor interop.
*   **Sitemap & Robots.txt:** These will likely be generated during the build process or managed via static files, integrated into the deployment pipeline.
```

# specs/3_Roadmap.md

```markdown
# 3_Roadmap.md

## Implementation Plan and Roadmap

This roadmap outlines the phased approach to implementing the required features and addressing missing components for the `test.vvgonline.net` project.

### Phase 1: Foundation and Core SEO Setup

*   **Task 1.1: Directory Setup**
    *   **Description:** Create the `specs/` directory within the `test.vvgonline.net` project structure.
    *   **Status:** Completed.
    *   **Artifacts:** `test.vvgonline.net/specs/`
*   **Task 1.2: Documentation Creation**
    *   **Description:** Create foundational documentation files within the `specs/` directory.
    *   **Status:** In Progress.
    *   **Artifacts:** `0_Project_Vision.md`, `1_Product_Requirements.md`, `2_Architecture.md`, `3_Roadmap.md`.
*   **Task 1.3: Essential SEO JSON Files**
    *   **Description:** Create `metadata.json`, `twitter-card.json`, and `open-graph.json` in `src/wwwroot/data/`.
    *   **Details:** Populate these files with relevant default metadata. Verify `MetadataService.cs` correctly loads these files.
    *   **Status:** Pending.
    *   **Artifacts:** `src/wwwroot/data/metadata.json`, `src/wwwroot/data/twitter-card.json`, `src/wwwroot/data/open-graph.json`.
*   **Task 1.4: Sitemap and Robots.txt**
    *   **Description:** Generate `sitemap.xml` and `robots.txt`.
    *   **Details:** Investigate current deployment process (GitHub Actions) for potential integration of these file generations or create them as static assets.
    *   **Status:** Pending.
    *   **Artifacts:** `sitemap.xml`, `robots.txt`.

### Phase 2: Feature Implementation

*   **Task 2.1: Blog Search and Filtering**
    *   **Description:** Implement client-side search and filtering logic on the `Blog.razor` page.
    *   **Dependencies:** Task 1.2 (Product Requirements). Task 1.3 (SEO files can be done in parallel).
    *   **Status:** Pending.
    *   **Artifacts:** Updates to `Blog.razor`, potentially new helper methods in services.
*   **Task 2.2: Theme Toggle**
    *   **Description:** Implement the UI toggle and persistence logic for theme switching.
    *   **Dependencies:** Core styling in `app.css` (assumed complete based on README).
    *   **Status:** Pending.
    *   **Artifacts:** Theme toggle component/logic, `localStorage` integration.
*   **Task 2.3: Enhance Hero Banners**
    *   **Description:** Refine `HeroBanner.razor` for full-screen (100vh) display and add animations/SVG patterns.
    *   **Dependencies:** Core CSS and asset availability.
    *   **Status:** Pending.
    *   **Artifacts:** Updated `HeroBanner.razor`.
*   **Task 2.4: Implement Charts**
    *   **Description:** Integrate `Chart.razor` component, connecting it to `facts-figures.json` via JavaScript interop.
    *   **Dependencies:** `facts-figures.json` must be populated.
    *   **Status:** Pending.
    *   **Artifacts:** Implemented `Chart.razor`, data binding.
*   **Task 2.5: Blog Content Model and Index**
    *   **Description:** Define the markdown + front‑matter structure for blog posts and implement the build‑time process that generates `blog-index.json` (and optional search index).
    *   **Dependencies:** Existing blog content scraping and markdown export must be available.
    *   **Status:** Pending.
    *   **Artifacts:** `wwwroot/blog/*.md`, `wwwroot/data/blog-index.json`, build script or CI step.
*   **Task 2.6: Blog Layouts**
    *   **Description:** Implement `BlogLayout.razor` separate from `MainLayout.razor`, with a two‑column layout and sidebar used by `/blog`, `/archives`, and `/blog/{slug}`.
    *   **Dependencies:** Core routing and base layout must be stable.
    *   **Status:** Pending.
    *   **Artifacts:** `BlogLayout.razor`, updates to routing and layout assignment.
*   **Task 2.7: Blog Index and Archives Pages**
    *   **Description:** Implement:
        * `Blog.razor` as the index page, reading from `blog-index.json` and showing a list of posts with basic tag filter.
        * `Archives.razor` with year/tag filters and search box.
    *   **Dependencies:** Task 2.5 (content model and index).
    *   **Status:** Pending.
    *   **Artifacts:** `Blog.razor`, `Archives.razor`, filter/search logic.
*   **Task 2.8: TOC and Sidebar Components**
    *   **Description:** Implement sidebar modules and a collapsible, scroll‑aware TOC for long posts.
    *   **Dependencies:** Single post view (`ViewPost.razor` or `/blog/{slug}` component) and heading structure must be defined.
    *   **Status:** Pending.
    *   **Artifacts:** `BlogToc.razor`, `BlogSidebarAbout.razor`, `BlogSidebarHighlights.razor`, `BlogSidebarTags.razor`, supporting JS interop for scrollspy.
*   **Task 2.9: Sharing and CTA**
    *   **Description:** Add simple “copy link” and optional share button on single posts and define an end‑of‑post CTA pattern.
    *   **Dependencies:** Single post layout and routing.
    *   **Status:** Pending.
    *   **Artifacts:** CTA component, copy/share UI in post template.


### Phase 3: Verification and Polish

*   **Task 3.1: PWA Functionality Verification**
    *   **Description:** Test offline capabilities and the PWA install prompt.
    *   **Dependencies:** Task 2.1 (general app stability).
    *   **Status:** Pending.
    *   **Artifacts:** Test report, potential fixes to `service-worker.js`.
*   **Task 3.2: Page-Specific SEO Verification**
    *   **Description:** Review key pages (Home, Services, Blog) to ensure dynamic meta tags are correctly set.
    *   **Dependencies:** Task 1.3 (SEO JSON files).
    *   **Status:** Pending.
    *   **Artifacts:** Verification report, code adjustments if needed.
*   **Task 3.3: Final Review and Testing**
    *   **Description:** Conduct a comprehensive review of all implemented features, code quality, and performance.
    *   **Dependencies:** All previous tasks.
    *   **Status:** Pending.
    *   **Artifacts:** Finalized code, updated documentation.
*   **Task 3.4: Blog UX and Navigation Review**
    *   **Description:** Validate usability of the blog index, archives filters, search box, sidebar, and TOC on desktop and mobile.
    *   **Dependencies:** Tasks 2.5–2.8.
    *   **Status:** Pending.
    *   **Artifacts:** UX review notes, backlog of refinements
*   **Task 3.5: Performance and Accessibility Audit (Blog)**
    *   **Description:** Measure load and interaction performance of blog views in Blazor WASM and verify accessibility (focus order, keyboard navigation, ARIA attributes for TOC and filters).
    *   **Dependencies:** All blog features implemented.
    *   **Status:** Pending.
    *   **Artifacts:** Performance profile, accessibility checklist, fixes.


This roadmap will be updated as implementation progresses and new information becomes available.
```

# specs/milestones/Milestones-9.md

```markdown
# Milestone 9: Blog Layout, Archives, and TOC

## Objectives
- Implement dedicated blog layouts and sidebar.
- Build archives with filters and search.
- Add TOC for long posts.

## Tasks

### 9.1 Blog Layouts
- [ ] Implement `BlogLayout.razor` distinct from `MainLayout.razor`.
- [ ] Configure routing so `/blog`, `/archives`, and `/blog/{slug}` use `BlogLayout`.
- [ ] Implement responsive 2-column grid (main + sidebar).

### 9.2 Blog Index and Single Post Views
- [ ] Update `Blog.razor` to use `BlogLayout` and `blog-index.json`.
- [ ] Implement single post view (`Post.razor` or route) that:
  - Loads markdown/HTML content for the specified slug.
  - Renders title, date, tags, and end-of-post CTA.
  - Shows related posts section.

### 9.3 Archives with Filters and Search
- [ ] Implement `Archives.razor` reading from `blog-index.json`.
- [ ] Add year filter (group and collapse by year).
- [ ] Add tag filter (chips or checkboxes).
- [ ] Add search box for title and content snippets.
- [ ] Ensure combined filter + search logic works correctly.

### 9.4 Sidebar and TOC
- [ ] Implement `BlogSidebarAbout.razor`, `BlogSidebarHighlights.razor`, `BlogSidebarTags.razor`.
- [ ] Implement `BlogToc.razor` that:
  - Builds a TOC from H2/H3 headings.
  - Supports collapse/expand.
  - Scrolls smoothly to sections.
  - Highlights active section (scrollspy).
- [ ] Integrate sidebar components into `BlogLayout.razor` with sensible ordering.
```

# .gemini/GEMINI.md

```markdown
# Gemini instructions

- for this codebase refer to readme.md
- for the theme used refer to folder
- always think step by step
- if you don't understand say 'I don't know'
- always confirm your thought process before giving me answers
- think deeply. no rush.
- ask for more context if you need it. i have no issue explaining my queries in length and depth.
- Always give concise responses
  -Always Prefer C# (csharp)
- Prefer TypeScript over JavaScript
- Prefer scss over css
- Prefer Blazor components over raw HTML
- Prefer Razor syntax over HTML where applicable
- when creating new files, always create them in the correct folder as per the project structure
- always follow the existing code style and conventions used in the codebase
- after I give command '/export', export the chat in markdown format without any additional commentary. file name should be 'chat_export<timestamp>.md'
```

# ../_scripts/blog_scraper.py

```python
#!/usr/bin/env python3
import os
import re
import json
from datetime import datetime
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# --- Configuration ---
BASE_URL = "https://vvgonline.net/"
BLOG_INDEX_URL = urljoin(BASE_URL, "#insights")
# The script will be in _scripts, so we go up one level and then to the target dir
OUTPUT_DIR_MD = "test.vvgonline.net/src/wwwroot/data/blog/"
OUTPUT_DIR_JSON = "test.vvgonline.net/src/wwwroot/data/"
BLOG_INDEX_JSON_FILE = os.path.join(OUTPUT_DIR_JSON, "blog-index.json")

def slugify(text):
    """
    Creates a URL-friendly slug from a string.
    """
    text = text.lower()
    text = re.sub(r'[\s\W-]+', '-', text)  # Replace spaces, non-word chars with a hyphen
    text = re.sub(r'^-+|-+$', '', text)     # Remove leading/trailing hyphens
    return text

def scrape_post_content(post_url):
    """
    Scrapes the title and content from an individual blog post page.
    """
    print(f"  Fetching post: {post_url}")
    try:
        response = requests.get(post_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # --- Content Extraction Logic ---
        # This needs to be adapted to the specific structure of the blog post HTML.
        # Based on vvgonline.net, the main content seems to be in a <section>
        # with a specific class or within the primary <main> element.
        # Let's try a broad approach first.
        article_body = soup.find('article') or soup.find('main')
        if not article_body:
            print(f"    [Warning] Could not find main article body for {post_url}. Skipping.")
            return None, None

        title_tag = article_body.find('h1')
        title = title_tag.get_text(strip=True) if title_tag else "Untitled"

        # Remove header, footer, nav, or any other unwanted sections from conversion
        for tag in article_body.select('header, footer, nav, .share-links, .related-posts'):
            tag.decompose()

        content_html = str(article_body)
        content_md = md(content_html, heading_style="ATX")

        return title, content_md
    except requests.RequestException as e:
        print(f"    [Error] Failed to fetch {post_url}: {e}")
        return None, None

def create_markdown_file(post_details):
    """
    Creates a markdown file with front-matter for a blog post.
    """
    slug = post_details['slug']
    filepath = os.path.join(OUTPUT_DIR_MD, f"{slug}.md")

    # Create front-matter
    front_matter = f"""
---
title: "{post_details['title']}"
slug: "{slug}"
publishedAt: "{post_details['publishedAt']}"
tags: {json.dumps(post_details['tags'])}
excerpt: "{post_details['excerpt']}"
draft: false
---

{post_details['content']}
"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(front_matter)
        print(f"  Successfully created {filepath}")
        return True
    except IOError as e:
        print(f"  [Error] Could not write file {filepath}: {e}")
        return False

def main():
    """
    Main function to orchestrate the scraping and file creation process.
    """
    print("Starting blog scraping process...")
    os.makedirs(OUTPUT_DIR_MD, exist_ok=True)
    os.makedirs(OUTPUT_DIR_JSON, exist_ok=True)

    try:
        print(f"Fetching main blog page: {BLOG_INDEX_URL}")
        response = requests.get(BLOG_INDEX_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[Error] Failed to fetch the main blog page. Aborting. {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    all_posts_metadata = []

    # --- Post Link Extraction Logic ---
    # This needs to be adapted to the HTML structure of the blog index page.
    # On vvgonline.net, posts are in <a> tags with a class like 'blog-link' or similar,
    # often wrapping a card or a title. Let's assume they are inside an element with id="insights".
    insights_section = soup.find(id="insights")
    if not insights_section:
        print("[Error] Could not find the #insights section. Aborting.")
        return

    # Find all links within the insights section
    post_links = insights_section.find_all('a', href=True)
    print(f"Found {len(post_links)} potential post links.")

    for link in post_links:
        post_href = link['href']
        
        # Simple filter to avoid nav links etc.
        if not post_href.startswith('Blog/') or post_href.endswith('.html') == False:
            continue
            
        full_url = urljoin(BASE_URL, post_href)
        title, content_md = scrape_post_content(full_url)

        if title and content_md:
            slug = slugify(title)
            # Create a simple excerpt
            excerpt = (content_md.split('\n\n')[0]).replace('"', '\"')
            
            post_metadata = {
                "title": title.replace('"', '\"'),
                "slug": slug,
                "publishedAt": datetime.now().isoformat(), # Placeholder date
                "tags": ["Scraped"], # Placeholder tag
                "excerpt": excerpt,
                "draft": False,
                "content": content_md
            }
            
            if create_markdown_file(post_metadata):
                # Don't include full content in the index
                del post_metadata['content']
                all_posts_metadata.append(post_metadata)

    if not all_posts_metadata:
        print("No posts were successfully scraped. Aborting index generation.")
        return

    # --- Generate blog-index.json ---
    print(f"\nCreating JSON index file: {BLOG_INDEX_JSON_FILE}")
    try:
        with open(BLOG_INDEX_JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_posts_metadata, f, indent=2)
        print("Successfully created blog-index.json.")
    except IOError as e:
        print(f"[Error] Failed to write JSON index file: {e}")

if __name__ == "__main__":
    main()
```

# src/Shared/SystemPanel.razor

```aspnetcorerazor
@inject IJSRuntime JS
@implements IDisposable

<nav class="system-panel">
    <NavLink href="" class="no-cursor"><img
            src="https://raw.githubusercontent.com/vvgonline/vvgonline/d6ce91fa38831bf3009b2070a2c9a0f323faa8f8/public/logo-2025.svg"
            alt="VVG ONLINE" class="vvg-logo-nav me-2"><span class="text-accent">&nbsp;VVG_ONLINE</span></NavLink>
    <NavLink href="Services" class="no-cursor"><i class="bi bi-cpu me-2"></i><span class="text-light">SERVICES</span>
    </NavLink>
    <NavLink href="About" class="no-cursor"><i class="bi bi-info-circle me-2"></i><span class="text-light">ABOUT</span>
    </NavLink>
    <NavLink href="Blog" class="no-cursor"><i class="bi bi-newspaper me-2"></i><span class="text-light">INSIGHTS</span>
    </NavLink>
    <NavLink href="Contact" class="no-cursor"><i class="bi bi-terminal me-2"></i><span class="text-light">CONTACT</span>
    </NavLink>
    <div class="status-right d-flex align-items-center">
        <button @onclick="ToggleTheme" class="btn btn-sm py-0 px-1 btn-theme" title="theme toggler">
            <i class="bi @(isDarkMode ? "bi-brightness-high-fill" : "bi-moon-fill")"></i>
        </button>

        <button id="nav-terminal-toggle" @onclick="() => Layout?.ToggleTerminal()"
            class="btn btn-sm py-0 px-1 btn-terminal" title="toggle terminal">
            <i class="bi bi-terminal"></i>&nbsp;F10
        </button>

        <span class="d-none d-md-inline">
            <span class="d-none d-md-inline">
                <span id="clock" class="text-center text-light bg-dark w-75 p-1">@currentTime</span>
            </span>
        </span>
    </div>
</nav>

@code {
    [CascadingParameter]
    public MainLayout? Layout { get; set; }

    private System.Timers.Timer? _timer;
    private string currentTime = "[ 00:00:00 ]";
    private bool isDarkMode = true;

    protected override async Task OnInitializedAsync()
    {
        _timer = new System.Timers.Timer(1000);
        _timer.Elapsed += (sender, args) => OnTimerElapsed();
        _timer.Start();

        var theme = await JS.InvokeAsync<string>("vvg.theme.current");
        isDarkMode = theme == "dark";
        await JS.InvokeVoidAsync("vvg.updateGridColor", theme);
    }

    private void OnTimerElapsed()
    {
        currentTime = $"[ {DateTime.Now:HH:mm:ss} ]";
        InvokeAsync(StateHasChanged);
    }

    private async Task ToggleTheme()
    {
        var theme = await JS.InvokeAsync<string>("vvg.theme.toggle");
        isDarkMode = theme == "dark";
        await JS.InvokeVoidAsync("vvg.updateGridColor", theme);
    }

    public void Dispose()
    {
        _timer?.Dispose();
    }
}
```
