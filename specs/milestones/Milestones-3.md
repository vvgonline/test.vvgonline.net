# Milestone 3: Blog and Search Foundations

## Objectives
- Stand up the basic blog listing.
- Implement initial search and tag filtering.

## Tasks

### 3. Blog Content Model and Storage
- [x] Scrape existing blog posts from `https://vvgonline.net` into markdown.
- [x] Normalize filenames and front-matter fields (title, slug, date, tags, excerpt, draft).
- [x] Store markdown files under `wwwroot/data/blogs`.
- [ ] Define a markdown content model for blog posts, including front-matter keys (`title`, `slug`, `publishedAt`, `tags`, `excerpt`, `draft`, `category`, `featured`).
- [ ] Create a build-time script to generate `blog-index.json` from the markdown front-matter.

### 3.1 Blog Index JSON
- [ ] Implement a build-time script or tool to generate a single `wwwroot/data/blog-index.json` from markdown front-matter for every markdown file in `wwwroot/data/blogs`.
- [ ] Include `title`, `slug`, `publishedAt`, `tags`, `excerpt`, `draft`, `category`, and `featured` fields in the index entries.
- [ ] Add this step to CI/CD so `blog-index.json` is always up-to-date.

### 3.2 Blog Listing with Search and Tag Filter
- [ ] Implement basic `Blog.razor`. This page should handle the listing, search, years and tag filtering. Tags (e.g. '# Digital', '# Blockchain') should be clickable to filter posts.
- [ ] Load `blog-index.json` and render a list of posts with title, date, tags, and excerpt.
- [ ] Add client-side search by title and excerpt.
- [ ] Add a tag filter (single or multi-select) above the list.
- [ ] Ensure the blog listing is responsive and accessible.
- [ ] Implement pagination if the post count exceeds a certain threshold (10 posts per page).

### 3.3 Individual Blog Post Page
- [ ] Implement `BlogPost.razor` to render individual blog posts based on slug.
- [ ] Load the corresponding markdown file from `wwwroot/data/blogs/{slug}.md` and render it as HTML.
- [ ] Include navigation links to previous/next posts based on publish date.
- [ ] Ensure proper SEO metadata (title, description) is set for each blog post page.

### 3.4 Archives, Filters, and Search
- [ ] Provide a dedicated archives view with year/tag filters and search.
- [ ] Implement the `Archives.razor` page with a search box at the top that filters posts by title and content.
- [ ] Add year filter functionality.
- [ ] Add tag filter functionality (single or multi-select).
- [ ] Display posts grouped by year, respecting active filters and search query.

### 3.5 Sidebar and Table of Contents (TOC)
- [ ] Provide a contextual sidebar with an optional collapsible TOC.
- [ ] Include about/profile card, highlights, tags, and optional TOC on single post pages.
- [ ] Generate the TOC from the post’s heading structure (H2/H3).
- [ ] Implement scrollspy functionality to highlight the currently visible section.

### 3.6 Interaction and Sharing
- [ ] Keep interaction minimal and focused on navigation and sharing.
- [ ] Add a “Copy link” action on single posts (copies canonical URL to clipboard).
- [ ] Implement a light-weight share button that triggers the browser’s native share dialog where supported.
- [ ] Include a clear call-to-action at the end of posts (e.g., “Contact VVG ONLINE” or “Explore services”).

## Additional Notes
- Ensure all changes are thoroughly tested and documented.
- Review and update any relevant documentation or user guides.
