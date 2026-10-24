#!/usr/bin/env python3
"""Generate the BizElec static pages from shared partials.

Edit content here, then run:  python3 build.py
Outputs index.html, services.html, about.html, projects.html, contact.html.
"""
from pathlib import Path

ROOT = Path(__file__).parent
PHONE = "(555) 123-4567"
PHONE_HREF = "tel:+15551234567"
EMAIL = "info@bizelec.com"

# ---------------------------------------------------------------------------
# Icons (Lucide-style, 24x24 stroke)
# ---------------------------------------------------------------------------
ICONS = {
    "zap": '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "headset": '<path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "home": '<path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V13h6v9"/>',
    "building": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M10 22v-4h4v4"/><path d="M9 6h.01M12 6h.01M15 6h.01M9 10h.01M12 10h.01M15 10h.01M9 14h.01M12 14h.01M15 14h.01"/>',
    "factory": '<path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/><path d="M17 18h1M12 18h1M7 18h1"/>',
    "panel": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 7h4v4H7zM7 15h4M7 18h4"/><path d="m15 7-1.5 4h3L15 16"/>',
    "bulb": '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6M10 22h4"/>',
    "ev": '<rect x="5" y="2" width="12" height="20" rx="2"/><path d="m12 6-3 6h4l-3 6"/><path d="M17 9h2a1 1 0 0 1 1 1v5a1.5 1.5 0 0 0 3 0"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "wifi": '<path d="M5 12.55a11 11 0 0 1 14.08 0M1.42 9a16 16 0 0 1 21.16 0M8.53 16.11a6 6 0 0 1 6.95 0M12 20h.01"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "handshake": '<path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.88-3.88a3 3 0 0 0-4.24 0l-.88.88a1 1 0 1 1-3-3l2.81-2.81a5.79 5.79 0 0 1 7.06-.87l.47.28a2 2 0 0 0 1.42.25L21 4"/><path d="m21 3 1 11h-2M3 3 2 14l6.5 6.5a1 1 0 1 0 3-3M3 4h8"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M8 14h.01M12 14h.01M16 14h.01M8 18h.01M12 18h.01M16 18h.01"/>',
    "calendar-sm": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "star": '<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "send": '<path d="m22 2-7 20-4-9-9-4z"/><path d="M22 2 11 13"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "map": '<path d="M3 6l6-3 6 3 6-3v15l-6 3-6-3-6 3z"/><path d="M9 3v15M15 6v15"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "close": '<path d="M18 6 6 18M6 6l12 12"/>',
}
FILLED = {
    "facebook": '<path d="M12 2a10 10 0 0 0-1.56 19.88v-7H7.9V12h2.54V9.8c0-2.5 1.49-3.89 3.78-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56V12h2.78l-.44 2.89h-2.34v7A10 10 0 0 0 12 2z"/>',
    "instagram": '<path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4z"/><path d="M16.5 2h-9A5.5 5.5 0 0 0 2 7.5v9A5.5 5.5 0 0 0 7.5 22h9a5.5 5.5 0 0 0 5.5-5.5v-9A5.5 5.5 0 0 0 16.5 2zm3.7 14.5a3.7 3.7 0 0 1-3.7 3.7h-9a3.7 3.7 0 0 1-3.7-3.7v-9a3.7 3.7 0 0 1 3.7-3.7h9a3.7 3.7 0 0 1 3.7 3.7z"/>',
    "linkedin": '<path d="M19 2H5a3 3 0 0 0-3 3v14a3 3 0 0 0 3 3h14a3 3 0 0 0 3-3V5a3 3 0 0 0-3-3zM8.3 18.3H5.6V9.8h2.7zM7 8.6a1.6 1.6 0 1 1 0-3.2 1.6 1.6 0 0 1 0 3.2zm11.3 9.7h-2.7v-4.1c0-1 0-2.3-1.4-2.3s-1.6 1.1-1.6 2.2v4.2H10V9.8h2.6V11c.4-.7 1.2-1.4 2.6-1.4 2.7 0 3.2 1.8 3.2 4.1z"/>',
    "phone-fill": '<path d="M20.5 15.6v3.1a2 2 0 0 1-2.2 2A18 18 0 0 1 3.3 5.7a2 2 0 0 1 2-2.2h3.1a1.5 1.5 0 0 1 1.5 1.3c.1.9.4 1.8.7 2.6a1.5 1.5 0 0 1-.3 1.6L8.9 10.4a15 15 0 0 0 4.7 4.7l1.4-1.4a1.5 1.5 0 0 1 1.6-.3c.8.3 1.7.6 2.6.7a1.5 1.5 0 0 1 1.3 1.5z"/>',
}


def ic(name, cls=""):
    if name in FILLED:
        return f'<svg class="icon icon--fill {cls}" viewBox="0 0 24 24" aria-hidden="true">{FILLED[name]}</svg>'
    extra = " icon--arrow" if name == "arrow" else ""
    return f'<svg class="icon{extra} {cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


def bolt(cls="logo__mark", uid="b"):
    return f'''<svg class="{cls}" viewBox="0 0 40 56" aria-hidden="true">
  <defs><linearGradient id="bolt-{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6aa8ff"/><stop offset="1" stop-color="#1a5be8"/></linearGradient></defs>
  <path d="M27 0 3 33h14l-6 23 26-35H22L31 0z" fill="url(#bolt-{uid})"/>
</svg>'''


def logo(uid):
    return f'''<a class="logo" href="index.html" aria-label="BizElec Electrical Services — home">
      {bolt(uid=uid)}
      <span class="logo__text"><span class="logo__name">Biz<span>Elec</span></span><span class="logo__tag">Electrical Services</span></span>
    </a>'''


NAV = [("index.html", "Home"), ("services.html", "Services"), ("about.html", "About"),
       ("projects.html", "Projects"), ("contact.html", "Contact")]


def header(active, light=False):
    links = "\n".join(
        f'          <li><a class="nav__link" href="{href}"{" aria-current=\"page\"" if href == active else ""}>{label}</a></li>'
        for href, label in NAV)
    return f'''<header class="site-header{' site-header--light' if light else ''}">
  <div class="container site-header__inner">
    {logo('h')}
    <nav class="nav" id="site-nav" aria-label="Primary">
      <ul class="nav__list">
{links}
      </ul>
      <a class="btn btn--primary nav__phone" href="{PHONE_HREF}">{ic('phone-fill')} Call {PHONE}</a>
    </nav>
    <a class="header-phone" href="{PHONE_HREF}">{ic('phone-fill')} {PHONE}</a>
    <button class="nav-toggle" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="Open menu">
      {ic('menu', 'icon--menu')}{ic('close', 'icon--close')}
    </button>
  </div>
</header>'''


def footer():
    links = "\n".join(f'          <li><a href="{h}">{l}</a></li>' for h, l in NAV)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="site-footer__top">
      {logo('f')}
      <nav class="footer-nav" aria-label="Footer">
        <ul>
{links}
        </ul>
      </nav>
      <div class="socials">
        <a href="#" aria-label="BizElec on Facebook">{ic('facebook')}</a>
        <a href="#" aria-label="BizElec on Instagram">{ic('instagram')}</a>
        <a href="#" aria-label="BizElec on LinkedIn">{ic('linkedin')}</a>
      </div>
    </div>
    <div class="site-footer__bottom">
      <span>&copy; <span data-year>2026</span> BizElec Electrical Services. All rights reserved.</span>
      <span>Safe<span class="sep">/</span>Reliable<span class="sep">/</span>Professional</span>
    </div>
  </div>
</footer>'''


def page(filename, title, description, body, light_header=False):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#081a3a">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 56'%3E%3Cpath d='M27 0 3 33h14l-6 23 26-35H22L31 0z' fill='%232373ff'/%3E%3C/svg%3E">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{header(filename, light_header)}
<main id="main">
{body}
</main>
{footer()}
<script src="js/main.js" defer></script>
</body>
</html>
'''
    (ROOT / filename).write_text(html)


def features(items, cls="feature", icon_cls="feature__icon"):
    return "\n".join(
        f'''      <div class="{cls}">
        {ic(icon, icon_cls)}
        <h3>{title}</h3>
        <p>{text}</p>
      </div>''' for icon, title, text in items)


FOUR_PROMISES = [
    ("shield", "Licensed &amp; Insured", "Your safety and peace<br>of mind come first."),
    ("zap", "Expert Technicians", "Skilled professionals<br>with years of experience."),
    ("clock", "On-Time Service", "We respect your time<br>and your schedule."),
    ("headset", "24/7 Emergency Support", "Because electrical issues<br>don&rsquo;t always wait."),
]

# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------
home = f'''<section class="hero">
  <div class="hero__media">
    <img src="images/hero-electrician.jpg" alt="BizElec electrician in a hard hat working on an electrical panel" width="504" height="600" fetchpriority="high">
  </div>
  <div class="container">
    <div class="hero__content">
      <p class="eyebrow">Safe<span>/</span>Reliable<span>/</span>Professional</p>
      <h1 class="h-display hero__title">Powering Your<br>Home &amp; Business<br><span class="text-blue">with Confidence</span></h1>
      <p class="hero__text">BizElec Electrical Services provides expert electrical solutions for residential, commercial, and industrial needs. From installations to repairs, we keep your power on and your property safe.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html">Get a Free Quote {ic('arrow')}</a>
        <a class="btn btn--outline btn--outline-light" href="services.html">Our Services</a>
      </div>
    </div>
  </div>
</section>

<section class="strip-band on-dark section--sm" aria-label="Why homeowners and businesses choose BizElec">
  <div class="container">
    <div class="feature-strip">
{features(FOUR_PROMISES)}
    </div>
  </div>
</section>

<section class="section on-dark">
  <div class="container split">
    <div class="split__media reveal">
      <div class="media-card">
        <img src="images/home-night.jpg" alt="Modern two-storey home with warm interior and landscape lighting at dusk" width="428" height="348" loading="lazy">
        <div class="media-badge">{ic('zap')} Residential<span>/</span>Commercial<span>/</span>Industrial</div>
      </div>
    </div>
    <div class="split__body reveal">
      <p class="eyebrow">Our Services</p>
      <h2 class="h-section">Complete Electrical Solutions</h2>
      <p class="lead">Whether you&rsquo;re building, upgrading, or need urgent repairs, BizElec Electrical Services has you covered. We offer a full range of electrical services designed to keep your property running safely and efficiently.</p>
      <ul class="check-list">
        <li>{ic('check')} Electrical Installations</li>
        <li>{ic('check')} Repairs &amp; Maintenance</li>
        <li>{ic('check')} Panel Upgrades</li>
        <li>{ic('check')} Commercial &amp; Industrial</li>
        <li>{ic('check')} Lighting Solutions</li>
        <li>{ic('check')} Smart Home Systems</li>
        <li>{ic('check')} EV Charger Installation</li>
        <li>{ic('check')} Safety Inspections</li>
      </ul>
      <div class="btn-row">
        <a class="btn btn--outline" href="services.html">View All Services {ic('arrow')}</a>
      </div>
    </div>
  </div>
</section>'''

# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------
SERVICES = [
    ("home", "Residential Electrical Services", "From panel upgrades to lighting, we keep your home safe, comfortable, and efficient."),
    ("building", "Commercial Electrical Services", "Reliable electrical solutions for offices, retail spaces, and business facilities."),
    ("factory", "Industrial Electrical Services", "Heavy-duty electrical systems built for performance and safety."),
    ("panel", "Panel Upgrades &amp; Replacements", "Increase capacity, improve safety, and power your future."),
    ("bulb", "Lighting Solutions", "Interior, exterior, and energy-efficient lighting for any space."),
    ("ev", "EV Charger Installation", "Charge into the future with professional EV charging station installation."),
    ("wrench", "Repairs &amp; Maintenance", "Fast, reliable service to keep your systems running smoothly."),
    ("shield", "Safety Inspections", "Identify issues early and ensure your system meets code and safety standards."),
    ("wifi", "Smart Home Systems", "Control, automate, and modernize your home or business."),
]
service_cards = "\n".join(f'''      <a class="service-card reveal" href="contact.html">
        <span class="service-card__icon">{ic(icon)}</span>
        <h3>{t}</h3>
        <p>{d}</p>
        <span class="service-card__link" aria-hidden="true">{ic('arrow')}</span>
      </a>''' for icon, t, d in SERVICES)

services = f'''<section class="hero hero--compact">
  <div class="hero__media">
    <img src="images/hero-electrician.jpg" alt="Licensed BizElec electrician servicing a breaker panel" width="504" height="600" fetchpriority="high">
  </div>
  <div class="container">
    <div class="hero__content">
      <p class="eyebrow">Our Services</p>
      <h1 class="h-display hero__title">Professional Electrical Services for <span class="text-blue">Homes, Businesses &amp; Industries</span></h1>
      <p class="hero__text">At BizElec Electrical Services, we provide a full range of electrical solutions designed to keep your property safe, efficient, and powered. From installations and upgrades to repairs and maintenance, our licensed electricians deliver quality work, on time, every time.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html">Get a Free Quote {ic('arrow')}</a>
        <a class="btn btn--outline btn--outline-light" href="projects.html">Our Projects</a>
      </div>
    </div>
  </div>
</section>

<section class="section on-light">
  <div class="container">
    <div class="intro-grid">
      <div>
        <p class="eyebrow">Our Services</p>
        <h2 class="h-section">Electrical Solutions for <span class="text-blue">Every Need</span></h2>
        <p class="lead">We offer a wide range of electrical services to meet the needs of residential, commercial, and industrial clients. No matter the size or complexity of the project, we&rsquo;ve got you covered.</p>
      </div>
      <div class="mini-features">
{features(FOUR_PROMISES, 'mini-feature', '')}
      </div>
    </div>
    <div class="service-grid">
{service_cards}
    </div>
  </div>
</section>

<section class="section--sm why on-dark">
  <div class="container why__grid">
    <div>
      <p class="eyebrow">Why Choose BizElec</p>
      <h2 class="h-section">Quality Work, Lasting <span class="text-blue">Results</span></h2>
      <p class="lead">We&rsquo;re more than just electricians &mdash; we&rsquo;re your long-term partner in safety, efficiency, and peace of mind. Our team is committed to delivering exceptional service, every project, no matter the size.</p>
      <div class="btn-row" style="margin-top:24px">
        <a class="btn btn--primary" href="about.html">Learn More About Us {ic('arrow')}</a>
      </div>
    </div>
    <span class="why__slash" aria-hidden="true"></span>
    <div class="why__cols">
{features([
    ("shield", "Experienced Team", "Skilled, certified, and ready for any project."),
    ("clock", "On-Time &amp; Reliable", "We show up when we say we will."),
    ("gear", "High-Quality Workmanship", "Built to last and meet code."),
    ("users", "Customer Focused", "Your satisfaction is our priority."),
], 'why__col', '')}
    </div>
  </div>
</section>

<section class="cta cta--light">
  <div class="cta__media">
    <img src="images/cta-house.jpg" alt="Modern home lit up at night" width="464" height="164" loading="lazy">
  </div>
  <div class="container">
    <div class="cta__inner">
      <p class="eyebrow">Ready to Get Started?</p>
      <h2 class="h-section">Need Electrical Service?<br>We&rsquo;re Here to Help.</h2>
      <p class="lead">Contact us today for a free quote or to schedule a service. Our team is ready to power your next project.</p>
      <div class="btn-row">
        <a class="btn btn--navy" href="{PHONE_HREF}">{ic('phone-fill')} {PHONE}</a>
        <a class="btn btn--outline" href="contact.html">Request a Quote {ic('arrow')}</a>
      </div>
    </div>
  </div>
</section>'''

# ---------------------------------------------------------------------------
# About
# ---------------------------------------------------------------------------
TEAM = [
    ("team-mike.jpg", "Mike Reynolds", "Lead Electrician"),
    ("team-sarah.jpg", "Sarah Mitchell", "Operations Manager"),
    ("team-daniel.jpg", "Daniel Carter", "Project Specialist"),
]
team_cards = "\n".join(f'''        <article class="team-card reveal">
          <img src="images/{img}" alt="Portrait of {name}, {role}" width="182" height="148" loading="lazy">
          <div class="team-card__body">
            <h3>{name}</h3>
            <p>{role}</p>
          </div>
        </article>''' for img, name, role in TEAM)

about = f'''<section class="hero hero--compact hero--wide-media">
  <div class="hero__media">
    <img src="images/about-hero-building.jpg" alt="Modern commercial building illuminated at dusk" width="584" height="306" fetchpriority="high">
  </div>
  <div class="container">
    <div class="hero__content">
      <p class="eyebrow">About Us</p>
      <h1 class="h-display hero__title">Powering Progress<br><span class="text-blue">Through Reliable</span><br>Electrical Solutions</h1>
      <p class="hero__text">At BizElec Electrical Services, we&rsquo;re more than just electricians &mdash; we&rsquo;re your trusted partner in creating safe, efficient, and high-performing spaces. With years of experience and a commitment to excellence, we deliver electrical solutions that keep homes, businesses, and communities powered.</p>
    </div>
  </div>
</section>

<section class="section on-light">
  <div class="container split">
    <div class="split__body reveal">
      <p class="eyebrow">Our Story</p>
      <h2 class="h-section">Built on Experience.<br>Driven by a Higher Standard.</h2>
      <p class="lead">BizElec Electrical Services was founded with a simple mission: provide high-quality electrical services with honesty, reliability, and a focus on customer satisfaction. What started as a small local operation has grown into a trusted name in residential, commercial, and industrial electrical services.</p>
      <p class="lead">Today, we&rsquo;re proud to serve our community with a team of skilled, certified electricians who bring expertise, professionalism, and a commitment to getting the job done right &mdash; the first time.</p>
      <div class="btn-row" style="margin-top:28px">
        <a class="btn btn--outline" href="#values">Our Mission &amp; Values {ic('arrow')}</a>
      </div>
    </div>
    <div class="split__media reveal">
      <div class="media-card media-card--light">
        <img src="images/about-electrician.jpg" alt="BizElec electrician inspecting wiring in a breaker panel" width="476" height="291" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="section--sm on-tint" id="values" aria-label="Our values">
  <div class="container">
    <div class="feature-strip">
{features([
    ("shield", "Safety First", "We prioritize safety in every project, for our team and your property."),
    ("users", "Customer Focused", "Your satisfaction is our priority, always."),
    ("gear", "Skilled Professionals", "Our team is trained, certified, and experienced."),
    ("handshake", "Integrity &amp; Trust", "We do what&rsquo;s right &mdash; no shortcuts, no surprises."),
])}
    </div>
  </div>
</section>

<section class="section--sm stats-band on-dark">
  <div class="container stats-grid">
    <div>
      <p class="eyebrow">By the Numbers</p>
      <h2 class="h-section">Experience You Can <span class="text-blue">Count On</span></h2>
    </div>
    <div class="stats">
      <div class="stat">{ic('calendar')}<strong>10+</strong><span>Years in Business</span></div>
      <div class="stat">{ic('zap')}<strong>500+</strong><span>Projects Completed</span></div>
      <div class="stat">{ic('users')}<strong>100%</strong><span>Licensed &amp; Insured</span></div>
      <div class="stat">{ic('star')}<strong>5.0</strong><span>Customer Satisfaction</span></div>
    </div>
  </div>
</section>

<section class="section on-light">
  <div class="container team-grid">
    <div>
      <p class="eyebrow">Our Team</p>
      <h2 class="h-section">Meet the People Behind <span class="text-blue">BizElec</span></h2>
      <p class="lead">Our team of licensed electricians and project experts bring a wealth of knowledge and hands-on experience to every job. We&rsquo;re passionate about what we do and take pride in delivering high-quality work and exceptional service.</p>
      <a class="btn btn--outline" href="contact.html">Meet Our Team {ic('arrow')}</a>
    </div>
    <div class="team-cards">
{team_cards}
    </div>
  </div>
</section>

<section class="cta cta--dark cta-bar">
  <div class="cta__media">
    <img src="images/cta-house.jpg" alt="" width="464" height="164" loading="lazy">
  </div>
  <div class="container cta-bar__inner">
    <div class="cta-bar__text">
      {bolt('cta-bar__bolt', 'cta')}
      <div>
        <h2 class="h-section">Ready to <span class="text-blue">Power</span> Your Next Project?</h2>
        <p class="lead">Whether you need a quick repair, a full installation, or ongoing maintenance, BizElec Electrical Services is here to help.</p>
      </div>
    </div>
    <a class="btn btn--primary" href="contact.html">Get a Free Quote {ic('arrow')}</a>
  </div>
</section>'''

# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------
FAQS = [
    ("Do you offer free estimates?", "Yes! We provide free, no-obligation estimates for all services."),
    ("Are you licensed and insured?", "Absolutely. We are fully licensed and insured for your protection."),
    ("What areas do you serve?", "We serve Riverside, CA and surrounding areas."),
    ("How soon can you schedule a service?", "We offer flexible scheduling, often same-day or next-day service."),
]
faq_items = "\n".join(f'''        <details open>
          <summary>{q}<span class="faq__toggle">{ic('plus')}</span></summary>
          <p>{a}</p>
        </details>''' for q, a in FAQS)

MAP_ART = '''<svg class="map__art" viewBox="0 0 470 320" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
        <rect width="470" height="320" fill="#eef2f8"/>
        <g stroke="#ffffff" stroke-width="7" fill="none" stroke-linecap="round">
          <path d="M-10 250 L480 120"/><path d="M60 -10 L170 330"/><path d="M200 -10 L260 330"/>
          <path d="M-10 90 L480 40"/><path d="M330 -10 L380 330"/><path d="M-10 190 L480 210"/>
        </g>
        <g stroke="#dfe6f1" stroke-width="2" fill="none">
          <path d="M-10 40 L480 10"/><path d="M-10 140 L480 90"/><path d="M-10 300 L480 260"/>
          <path d="M20 -10 L90 330"/><path d="M120 -10 L210 330"/><path d="M290 -10 L320 330"/><path d="M420 -10 L450 330"/>
          <path d="M-10 230 L480 170"/><path d="M240 -10 L300 330"/>
        </g>
        <path d="M480 150 C430 170 420 230 380 250 C330 275 300 240 260 270 C230 292 230 320 220 330" stroke="#a9c8f5" stroke-width="22" fill="none" stroke-linecap="round"/>
        <path d="M400 -10 C410 40 380 70 420 110 C440 130 470 140 480 150" stroke="#a9c8f5" stroke-width="14" fill="none"/>
        <g font-family="Inter, sans-serif" fill="#7b8aa6" font-size="10">
          <text x="140" y="104" transform="rotate(-14 140 104)">Magnolia Ave</text>
          <text x="345" y="58" transform="rotate(-24 345 58)">Central Ave</text>
          <text x="240" y="196" transform="rotate(-8 240 196)">Magnolia Ave</text>
        </g>
        <text x="245" y="240" font-family="Outfit, sans-serif" font-size="17" font-weight="500" fill="#2c3e60">Riverside</text>
      </svg>'''

contact = f'''<section class="hero hero--compact">
  <div class="hero__media">
    <img src="images/hero-electrician.jpg" alt="BizElec electrician working on a commercial electrical panel" width="504" height="600" fetchpriority="high">
  </div>
  <div class="container">
    <div class="hero__content">
      <p class="eyebrow">Contact Us</p>
      <h1 class="h-display hero__title">Get in Touch<br>We&rsquo;re Here to <span class="text-blue">Help</span></h1>
      <p class="hero__text">Have a question, need a quote, or looking for reliable electrical services? Our team is here to help. Reach out to us today &mdash; we&rsquo;ll get back to you as soon as possible.</p>
      <div class="hero-features">
{features([
    ("zap", "Fast Response", "We reply within 24 hours."),
    ("shield", "Trusted Experts", "Licensed &amp; insured professionals."),
    ("pin", "Local &amp; Reliable", "Proudly serving our community."),
    ("headset", "Friendly Support", "Real people, not bots."),
], 'hero-feature', '')}
      </div>
    </div>
  </div>
</section>

<section class="section on-light">
  <div class="container">
    <div class="contact-grid">
      <div class="card card--form reveal">
        <p class="eyebrow">Send Us a Message</p>
        <h2 class="h-section">How Can We Help You?</h2>
        <p>Fill out the form below and we&rsquo;ll get back to you shortly.</p>
        <form class="form" id="contact-form" action="#" method="post" novalidate>
          <div class="field">
            <label for="f-name">Full Name <span class="req" aria-hidden="true">*</span></label>
            <input id="f-name" name="name" type="text" autocomplete="name" placeholder="Your name" required aria-describedby="e-name">
            <span class="field__error" id="e-name">Please enter your name.</span>
          </div>
          <div class="field">
            <label for="f-email">Email Address <span class="req" aria-hidden="true">*</span></label>
            <input id="f-email" name="email" type="email" autocomplete="email" inputmode="email" placeholder="you@example.com" required aria-describedby="e-email">
            <span class="field__error" id="e-email">Please enter a valid email.</span>
          </div>
          <div class="field">
            <label for="f-phone">Phone Number <span class="req" aria-hidden="true">*</span></label>
            <input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" placeholder="{PHONE}" required aria-describedby="e-phone">
            <span class="field__error" id="e-phone">Please enter a 10-digit phone number.</span>
          </div>
          <div class="field">
            <label for="f-service">Service Needed</label>
            <select id="f-service" name="service">
              <option value="">Select a service</option>
              <option>Residential Electrical</option>
              <option>Commercial Electrical</option>
              <option>Industrial Electrical</option>
              <option>Panel Upgrade</option>
              <option>Lighting Solutions</option>
              <option>EV Charger Installation</option>
              <option>Repairs &amp; Maintenance</option>
              <option>Safety Inspection</option>
              <option>Smart Home Systems</option>
              <option>Emergency Service</option>
            </select>
          </div>
          <div class="field field--full">
            <label for="f-message">Message <span class="req" aria-hidden="true">*</span></label>
            <textarea id="f-message" name="message" placeholder="Tell us about your project or request..." required aria-describedby="e-message"></textarea>
            <span class="field__error" id="e-message">Please tell us a little about your project.</span>
          </div>
          <div class="form__actions">
            <button class="btn btn--primary" type="submit">{ic('send')} Send Message {ic('arrow')}</button>
            <p class="form__status" role="status" aria-live="polite"></p>
          </div>
        </form>
      </div>

      <div class="contact-info reveal">
        <p class="eyebrow">Our Contact Information</p>
        <h2 class="h-section">Let&rsquo;s Connect</h2>
        <ul class="info-list">
          <li class="info-item"><span class="info-item__icon">{ic('phone-fill')}</span><div><h3>Phone</h3><a href="{PHONE_HREF}">{PHONE}</a><small>Mon &ndash; Fri: 7:00 AM &ndash; 6:00 PM</small></div></li>
          <li class="info-item"><span class="info-item__icon">{ic('mail')}</span><div><h3>Email</h3><a href="mailto:{EMAIL}">{EMAIL}</a><small>We&rsquo;ll respond within 24 hours</small></div></li>
          <li class="info-item"><span class="info-item__icon">{ic('pin')}</span><div><h3>Office Location</h3><p>123 Power Lane</p><small>Riverside, CA 92507</small></div></li>
          <li class="info-item"><span class="info-item__icon">{ic('clock')}</span><div><h3>Emergency Service</h3><a href="{PHONE_HREF}">{PHONE}</a><small>Available 24/7</small></div></li>
        </ul>
      </div>

      <aside class="emergency-card reveal">
        <div class="emergency-card__media">
          <img src="images/emergency-building.jpg" alt="" width="202" height="223" loading="lazy">
        </div>
        <div class="emergency-card__body">
          {ic('zap')}
          <h3>Emergency Electrical Services Available</h3>
          <p>Power issues don&rsquo;t wait.<br>Neither do we.</p>
          <a class="btn btn--outline btn--outline-light" href="{PHONE_HREF}">Call Now {ic('arrow')}</a>
        </div>
      </aside>
    </div>

    <div class="map-faq">
      <div class="map reveal">
        {MAP_ART}
        <svg class="map__pin" viewBox="0 0 24 30" aria-hidden="true"><path d="M12 0a11 11 0 0 0-11 11c0 8 11 19 11 19s11-11 11-19A11 11 0 0 0 12 0z" fill="currentColor"/><circle cx="12" cy="11" r="4" fill="#fff"/></svg>
        <div class="map__card">
          {ic('map')}
          <h3>Find Us</h3>
          <p>123 Power Lane<br>Riverside, CA 92507</p>
          <a class="btn btn--outline" href="https://www.google.com/maps/search/?api=1&amp;query=123+Power+Lane+Riverside+CA+92507" target="_blank" rel="noopener">Get Directions {ic('arrow')}</a>
        </div>
      </div>
      <div class="faq reveal">
        <p class="eyebrow">Frequently Asked Questions</p>
        <h2 class="h-section">Quick Answers</h2>
{faq_items}
      </div>
    </div>
  </div>
</section>

<section class="cta cta--dark">
  <div class="cta__media">
    <img src="images/cta-house.jpg" alt="" width="464" height="164" loading="lazy">
  </div>
  <div class="container">
    <div class="cta__inner">
      <p class="eyebrow">Ready to Get Started?</p>
      <h2 class="h-section">Your Project. Our Priority.</h2>
      <p class="lead">Contact us today for a free quote or to schedule a service.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="{PHONE_HREF}">{ic('phone-fill')} {PHONE}</a>
        <a class="btn btn--outline" href="#contact-form">Request a Quote {ic('arrow')}</a>
      </div>
    </div>
  </div>
</section>'''

# ---------------------------------------------------------------------------
# Projects
# ---------------------------------------------------------------------------
PROJECTS = [
    ("residential", "Residential", "project-custom-home.jpg", "Custom Home Electrical Installation",
     "Complete electrical installation for a newly built custom home, including lighting, outlets, panel setup, and smart home integration.",
     "Riverside, CA", "2024"),
    ("commercial", "Commercial", "project-office.jpg", "Office Building Fit-Out",
     "Full electrical fit-out for a 12,000 sq. ft. office space, including lighting, power distribution, networking, and emergency systems.",
     "San Bernardino, CA", "2024"),
    ("industrial", "Industrial", "project-warehouse.jpg", "Warehouse Electrical Upgrade",
     "Upgraded electrical systems for a 50,000 sq. ft. warehouse, including high-bay lighting, panel upgrades, and machinery connections.",
     "Fontana, CA", "2023"),
    ("renovations residential", "Renovation", "project-panel.jpg", "Panel Upgrade &ndash; Residential",
     "Replaced outdated electrical panel and wiring for improved safety, capacity, and efficiency in an existing home.",
     "Temecula, CA", "2023"),
    ("commercial", "Commercial", "project-restaurant.jpg", "Restaurant Electrical Installation",
     "Installed complete electrical system for a new restaurant, including kitchen equipment, lighting, and indoor/outdoor power.",
     "Murrieta, CA", "2023"),
    ("residential emergency", "Sustainable Energy", "project-solar.jpg", "Solar Panel &amp; EV Charger Setup",
     "Installed solar panels with battery backup and EV charging station for a residential property.",
     "Menifee, CA", "2022"),
]
project_cards = "\n".join(f'''      <article class="project-card reveal" data-category="{cat}">
        <div class="project-card__media"><img src="images/{img}" alt="{title.replace('&ndash;', '-').replace('&amp;', 'and')}" width="300" height="182" loading="lazy"></div>
        <div class="project-card__body">
          <span class="project-card__tag">{tag}</span>
          <h3>{title}</h3>
          <p>{desc}</p>
          <div class="project-card__meta">
            <span>{ic('pin')} {loc}</span>
            <span>{ic('calendar-sm')} Completed {year}</span>
            <a href="contact.html" aria-label="Start a project like {title.replace('&ndash;', '-').replace('&amp;', 'and')}">{ic('arrow')}</a>
          </div>
        </div>
      </article>''' for cat, tag, img, title, desc, loc, year in PROJECTS)

FILTERS = [("all", "All Projects"), ("residential", "Residential"), ("commercial", "Commercial"),
           ("industrial", "Industrial"), ("renovations", "Renovations"), ("emergency", "Emergency")]
filter_btns = "\n".join(
    f'      <button class="filter-btn" type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{l}</button>'
    for k, l in FILTERS)

projects = f'''<section class="hero hero--compact hero--wide-media">
  <div class="hero__media">
    <img src="images/projects-hero-building.jpg" alt="Two-storey glass office building lit up at twilight" width="604" height="324" fetchpriority="high">
  </div>
  <div class="container">
    <div class="hero__content">
      <p class="eyebrow">Our Projects</p>
      <h1 class="h-display hero__title">Real Projects.<br>Reliable <span class="text-blue">Results.</span></h1>
      <p class="hero__text">From residential upgrades to large-scale commercial installations, explore some of the projects we&rsquo;ve completed and the lasting impact of our electrical solutions.</p>
      <div class="hero-features hero-features--3">
{features([
    ("gear", "Quality<br>Workmanship", ""),
    ("clock", "On-Time<br>Delivery", ""),
    ("headset", "Safe &amp; Code<br>Compliant", ""),
], 'hero-feature', '').replace('        <p></p>\n', '')}
      </div>
    </div>
  </div>
</section>

<section class="section on-light">
  <div class="container">
    <div class="filters" role="group" aria-label="Filter projects">
{filter_btns}
    </div>
    <div class="project-grid">
{project_cards}
    </div>
  </div>
</section>

<section class="cta cta--dark cta--split">
  <div class="cta__media">
    <img src="images/ev-charger.jpg" alt="" width="324" height="107" loading="lazy">
  </div>
  <div class="container cta__layout">
    <div class="cta__inner">
      <p class="eyebrow">Ready to Start Your Project?</p>
      <h2 class="h-section">Let&rsquo;s Build Something <span class="text-blue">Great.</span></h2>
      <p class="lead">Whether it&rsquo;s a small repair or a large-scale installation, BizElec Electrical Services is here to help. Contact us today for a free quote and expert advice.</p>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html">Get a Free Quote {ic('arrow')}</a>
      </div>
    </div>
    <div class="cta-stats">
      <div class="cta-stat">{ic('zap')}<strong>10+</strong><span>Years of Experience</span></div>
      <div class="cta-stat">{ic('users')}<strong>500+</strong><span>Projects Completed</span></div>
      <div class="cta-stat">{ic('shield')}<strong>100%</strong><span>Customer Satisfaction</span></div>
    </div>
  </div>
</section>'''

page("index.html", "BizElec Electrical Services | Residential, Commercial & Industrial Electricians",
     "Licensed and insured electricians for homes and businesses. Installations, panel upgrades, EV chargers, repairs, and 24/7 emergency service.", home)
page("services.html", "Electrical Services | BizElec Electrical Services",
     "Residential, commercial, and industrial electrical services: panel upgrades, lighting, EV chargers, repairs, inspections, and smart home systems.", services)
page("about.html", "About Us | BizElec Electrical Services",
     "Meet BizElec Electrical Services: 10+ years, 500+ projects, fully licensed and insured electricians serving Riverside, CA.", about)
page("projects.html", "Our Projects | BizElec Electrical Services",
     "Explore residential, commercial, and industrial electrical projects completed by BizElec Electrical Services.", projects, light_header=True)
page("contact.html", "Contact Us | BizElec Electrical Services",
     "Get a free quote or schedule electrical service. Call (555) 123-4567 — 24/7 emergency service available.", contact)
print("Built 5 pages.")
