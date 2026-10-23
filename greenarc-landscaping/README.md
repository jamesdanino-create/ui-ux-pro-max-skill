# Greenarc Landscaping — Website

Static, mobile-friendly marketing site built from the Greenarc mockups. No build step.

## Pages
- `index.html` — Home (hero, services, gallery, reviews, contact form)
- `services.html` — Services grid, process, CTA
- `contact.html` — Contact info, quote form, map, values
- `about.html` — Story, values, team, mission & vision

Gallery and Reviews in the nav link to sections on the home page.

## Structure
```
assets/css/styles.css   # all styles (design tokens at the top, breakpoints at 1100/960/640px)
assets/js/main.js       # icon sprite, mobile menu, scroll reveal, form handling
assets/img/             # photos (cropped from the mockups — swap in full-resolution originals)
```

## Before going live
- **Photos:** images in `assets/img/` were cropped from the mockup files, so they're low resolution. Replace them with the original photos using the same filenames.
- **Forms:** the quote forms validate in the browser and show a thank-you message, but don't send anything yet. Add an `action="https://formspree.io/f/…"` (or a similar endpoint) to each `<form class="quote-form">` and the script will POST to it.
- **Links:** social icons and the Privacy/Terms links point to `#`.

## Preview
Open `index.html` in a browser, or run `python3 -m http.server` in this folder.
