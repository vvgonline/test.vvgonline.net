# Milestone 3: Blog and Search Foundations

## Objectives
- Stand up the basic blog listing.
- Implement initial search and tag filtering.

## Tasks

### 3.1 Blog Data Extraction
- [ ] Scrape existing blog posts from `https://vvgonline.net` into markdown.
- [ ] Normalize filenames and front-matter fields (title, slug, date, tags, excerpt, draft).
- [ ] Store markdown files under `wwwroot/blog/` or `wwwroot/data/blog/`.

### 3.2 Blog Index JSON
- [ ] Implement a build-time script or tool to generate `wwwroot/data/blog-index.json` from markdown front-matter.
- [ ] Include `title`, `slug`, `publishedAt`, `tags`, `excerpt`, `draft` in the index entries.
- [ ] Add this step to CI/CD so `blog-index.json` is always up to date.

### 3.3 Blog Listing with Search and Tag Filter
- [ ] Implement basic `Blog.razor` using `MainLayout.razor` (temporary).
- [ ] Load `blog-index.json` and render a list of posts with title, date, tags, and excerpt.
- [ ] Add client-side search by title and excerpt.
- [ ] Add a tag filter (single or multi-select) above the list.