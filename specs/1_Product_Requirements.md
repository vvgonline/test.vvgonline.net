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
    * **Scrap current blog posts from the existing blog section:** Extract existing blog posts from the current blog section of the [site](https://vvgonline.net/#insights) to populate the new blog structure.

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