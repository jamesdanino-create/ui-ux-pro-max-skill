# BizElec Electrical Services — Website

Static, mobile-friendly 5-page site (Home, Services, About, Projects, Contact) built from the BizElec mockups.

- Open `index.html` in a browser — no build step or server required.
- Content and shared header/footer live in `build.py`; edit there and run `python3 build.py` to regenerate the HTML pages.
- Styles: `css/styles.css` (breakpoints at 1100px, 960px, 640px). Interactions: `js/main.js` (mobile menu, project filters, form validation, scroll reveal).
- Images in `images/` were cropped from the mockups as placeholders; swap in full-resolution photography before launch.
- The contact form validates client-side only. Point its `action` at a form backend (Formspree, Netlify Forms, etc.) to deliver messages.

## Deploying to Vercel

1. In Vercel, choose **Add New → Project** and import this GitHub repository.
2. Set **Root Directory** to `bizelec-website`. Leave Framework Preset as **Other** with no build command (`vercel.json` already configures this).
3. Click **Deploy**. Every push to the repo redeploys automatically; pushes to non-production branches get preview URLs.

`cleanUrls` serves pages without `.html` (e.g. `/services`). `build.py` and this README are excluded from the deployment via `.vercelignore`.
