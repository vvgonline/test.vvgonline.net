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

### Integration of New Features

*   **SEO JSON Files:** New JSON files (`metadata.json`, `twitter-card.json`, `open-graph.json`) will be placed in `src/wwwroot/data/` and referenced by `MetadataService.cs`.
*   **Blog Search & Filter:** Logic will be added to `Blog.razor` to filter and search `blog-posts.json` data client-side.
*   **Theme Toggle:** A new component or logic within existing layout components will manage theme state (using `localStorage`) and apply CSS classes accordingly.
*   **Animated Hero Banners:** The existing `HeroBanner.razor` will be enhanced with CSS animations and potentially JavaScript interop for advanced effects.
*   **Charts:** The `Chart.razor` component will be implemented to consume data from `facts-figures.json` and render charts using a JavaScript charting library (e.g., Chart.js) via Blazor interop.
*   **Sitemap & Robots.txt:** These will likely be generated during the build process or managed via static files, integrated into the deployment pipeline.
