(function () {
  'use strict';

  /* Mobile navigation */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('main-nav');
  if (toggle && nav) {
    var setOpen = function (open) {
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      toggle.querySelector('.i-menu').style.display = open ? 'none' : '';
      toggle.querySelector('.i-close').style.display = open ? '' : 'none';
    };
    toggle.addEventListener('click', function () {
      setOpen(!nav.classList.contains('is-open'));
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) { setOpen(false); toggle.focus(); }
    });
    document.addEventListener('click', function (e) {
      if (nav.classList.contains('is-open') && !nav.contains(e.target) && !toggle.contains(e.target)) setOpen(false);
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 920) setOpen(false);
    });
  }

  /* Footer year */
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  /* Scroll reveal */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('is-visible'); io.unobserve(entry.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* Gallery filter */
  var filterBtns = document.querySelectorAll('.filter-btn');
  var items = Array.prototype.slice.call(document.querySelectorAll('.gallery-grid .gallery-item'));
  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var f = btn.getAttribute('data-filter');
      filterBtns.forEach(function (b) {
        var active = b === btn;
        b.classList.toggle('is-active', active);
        b.setAttribute('aria-pressed', String(active));
      });
      items.forEach(function (item) {
        var cats = (item.getAttribute('data-category') || '').split(' ');
        item.classList.toggle('is-hidden', f !== 'all' && cats.indexOf(f) === -1);
      });
    });
  });

  /* Lightbox */
  var lb = document.getElementById('lightbox');
  if (lb) {
    var lbImg = lb.querySelector('img');
    var lbCap = lb.querySelector('figcaption');
    var current = 0;
    var lastFocus = null;
    var visible = function () { return items.filter(function (i) { return !i.classList.contains('is-hidden'); }); };
    var show = function (idx) {
      var list = visible();
      if (!list.length) return;
      current = (idx + list.length) % list.length;
      var img = list[current].querySelector('img');
      lbImg.src = img.src;
      lbImg.alt = img.alt;
      lbCap.textContent = list[current].getAttribute('data-title') || img.alt;
    };
    var open = function (item) {
      lastFocus = document.activeElement;
      show(visible().indexOf(item));
      lb.classList.add('is-open');
      document.body.style.overflow = 'hidden';
      lb.querySelector('.lb-close').focus();
    };
    var close = function () {
      lb.classList.remove('is-open');
      document.body.style.overflow = '';
      if (lastFocus) lastFocus.focus();
    };
    items.forEach(function (item) { item.addEventListener('click', function () { open(item); }); });
    lb.querySelector('.lb-close').addEventListener('click', close);
    lb.querySelector('.lb-prev').addEventListener('click', function () { show(current - 1); });
    lb.querySelector('.lb-next').addEventListener('click', function () { show(current + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(current - 1);
      if (e.key === 'ArrowRight') show(current + 1);
    });
  }

  /* Contact form validation */
  var form = document.getElementById('contact-form');
  if (form) {
    var rules = {
      name: function (v) { return v.trim().length >= 2 || 'Please enter your name.'; },
      email: function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) || 'Please enter a valid email address.'; },
      phone: function (v) { return v.replace(/[^\d]/g, '').length >= 8 || 'Please enter a valid phone number.'; },
      message: function (v) { return v.trim().length >= 5 || 'Please tell us a little about your project.'; }
    };
    var validate = function (input) {
      var rule = rules[input.name];
      if (!rule) return true;
      var res = rule(input.value);
      var field = input.closest('.field');
      var err = field.querySelector('.error');
      if (res === true) {
        field.classList.remove('has-error');
        input.removeAttribute('aria-invalid');
        return true;
      }
      field.classList.add('has-error');
      input.setAttribute('aria-invalid', 'true');
      err.textContent = res;
      return false;
    };
    Object.keys(rules).forEach(function (name) {
      var input = form.elements[name];
      input.addEventListener('blur', function () { if (input.value) validate(input); });
      input.addEventListener('input', function () {
        if (input.closest('.field').classList.contains('has-error')) validate(input);
      });
    });
    form.addEventListener('submit', function (e) {
      var firstBad = null;
      Object.keys(rules).forEach(function (name) {
        var input = form.elements[name];
        if (!validate(input) && !firstBad) firstBad = input;
      });
      if (firstBad) { e.preventDefault(); firstBad.focus(); return; }

      // No form endpoint configured yet: show a confirmation instead of submitting.
      // To receive enquiries, set the form's action to a form service (e.g. Formspree)
      // and remove the data-demo attribute.
      if (form.hasAttribute('data-demo')) {
        e.preventDefault();
        var ok = document.getElementById('form-success');
        ok.classList.add('is-visible');
        form.reset();
        ok.focus();
      }
    });
  }
})();
