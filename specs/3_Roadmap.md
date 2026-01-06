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

This roadmap will be updated as implementation progresses and new information becomes available.
