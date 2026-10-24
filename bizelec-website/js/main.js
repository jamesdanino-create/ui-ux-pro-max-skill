// BizElec Electrical Services — site interactions
(function () {
  "use strict";

  // Mobile navigation
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".nav-toggle");
  if (header && toggle) {
    var setOpen = function (open) {
      header.classList.toggle("nav-open", open);
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    };
    toggle.addEventListener("click", function () {
      setOpen(!header.classList.contains("nav-open"));
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && header.classList.contains("nav-open")) {
        setOpen(false);
        toggle.focus();
      }
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 960) setOpen(false);
    });
  }

  // Reveal on scroll
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealEls.forEach(function (el) {
      if (el.getBoundingClientRect().top > window.innerHeight) {
        el.classList.add("is-pending");
        io.observe(el);
      }
    });
  }

  // Project filters
  var filterBtns = document.querySelectorAll(".filter-btn");
  var projects = document.querySelectorAll(".project-card");
  filterBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var filter = btn.getAttribute("data-filter");
      filterBtns.forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
      projects.forEach(function (card) {
        var cats = (card.getAttribute("data-category") || "").split(" ");
        card.hidden = filter !== "all" && cats.indexOf(filter) === -1;
      });
    });
  });

  // Contact form (client-side validation; wire `action` to a form backend to deliver messages)
  var form = document.querySelector("#contact-form");
  if (form) {
    var status = form.querySelector(".form__status");
    var validators = {
      name: function (v) { return v.trim().length > 1; },
      email: function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()); },
      phone: function (v) { return v.replace(/\D/g, "").length >= 10; },
      message: function (v) { return v.trim().length > 4; }
    };
    var check = function (input) {
      var fn = validators[input.name];
      if (!fn) return true;
      var ok = fn(input.value);
      input.closest(".field").classList.toggle("has-error", !ok);
      input.setAttribute("aria-invalid", String(!ok));
      return ok;
    };
    form.addEventListener("input", function (e) {
      if (e.target.closest(".field.has-error")) check(e.target);
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var firstBad = null;
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!check(el) && !firstBad) firstBad = el;
      });
      if (firstBad) {
        firstBad.focus();
        status.textContent = "";
        return;
      }
      form.reset();
      status.textContent = "Thanks! Your message has been sent — we'll reply within 24 hours.";
    });
  }

  // Footer year
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
