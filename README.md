# rendercheck

**rendercheck** is a lightweight web analysis tool that detects whether a given web page relies on JavaScript for rendering its meaningful content. It helps developers, SEO analysts, and automation tools identify pages that are invisible to static crawlers or bots.

---

## Features

- Detects pages that render no meaningful HTML content without JavaScript
- Uses structural heuristics (e.g. empty `#root`/`#app`, low text density)
- Outputs response metadata: word count, content tags, script weight
- Works as a static fetcher — no browser or JavaScript runtime required
- Suitable for large-scale analysis or integration into audit pipelines

---

## Use Cases

- SEO audits to flag JS-only pages
- Static site validation
- Web accessibility and discoverability checks
- Pre-rendering diagnostics
