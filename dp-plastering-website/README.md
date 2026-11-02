# DP Plastering and Painting Services — Website

Static, mobile-friendly website (HTML/CSS/vanilla JS, no build step).

Pages: `index.html` (Home), `services.html`, `gallery.html`, `reviews.html`, `contact.html`.

## Preview
Open `index.html` in a browser, or run `python3 -m http.server` in this folder and visit http://localhost:8000.

## Before going live
- **Contact form:** currently shows a confirmation without sending. Point the form's `action` at a form service
  (e.g. Formspree, or add `data-netlify="true"` on Netlify) and remove the `data-demo` attribute in `contact.html`.
- **Details:** phone, email and social links (Facebook/Instagram/Google) are placeholders from the mockups.
- **Reviews & photos:** replace sample reviews, avatars and project photos with genuine customer reviews and your own job photos.
- **Map:** the "Get Directions" link searches Google Maps for the business name; swap in your Google Business Profile link.
