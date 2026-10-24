# BizElec Electrical Services — Website

Static, mobile-friendly 5-page site (Home, Services, About, Projects, Contact) built from the BizElec mockups.

- Open `index.html` in a browser — no build step or server required.
- Content and shared header/footer live in `build.py`; edit there and run `python3 build.py` to regenerate the HTML pages.
- Styles: `css/styles.css` (breakpoints at 1100px, 960px, 640px). Interactions: `js/main.js` (mobile menu, project filters, form validation, scroll reveal).
- Images in `images/` were cropped from the mockups as placeholders; swap in full-resolution photography before launch.
- The contact form validates client-side only. Point its `action` at a form backend (Formspree, Netlify Forms, etc.) to deliver messages.
