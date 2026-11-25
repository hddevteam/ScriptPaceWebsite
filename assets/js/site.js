(function () {
  "use strict";

  function preferredLocale() {
    var languages = navigator.languages || [navigator.language || "en"];
    return languages.some(function (language) {
      return String(language).toLowerCase().indexOf("zh") === 0;
    }) ? "zh-hans" : "en";
  }

  function initLocaleRedirect() {
    var rootPage = document.body && document.body.hasAttribute("data-root-page");
    if (!rootPage || sessionStorage.getItem("scriptpace-root-visited")) {
      return;
    }
    sessionStorage.setItem("scriptpace-root-visited", "1");
    window.location.replace(preferredLocale() + "/");
  }

  function initMobileNavigation() {
    var toggle = document.querySelector("[data-menu-toggle]");
    var menu = document.querySelector("[data-mobile-menu]");
    if (!toggle || !menu) {
      return;
    }
    function closeMenu(restoreFocus) {
      if (toggle.getAttribute("aria-expanded") !== "true") {
        return;
      }
      toggle.setAttribute("aria-expanded", "false");
      menu.hidden = true;
      if (restoreFocus) {
        toggle.focus();
      }
    }
    toggle.addEventListener("click", function () {
      var expanded = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!expanded));
      menu.hidden = expanded;
    });
    menu.addEventListener("click", function (event) {
      if (event.target.closest("a")) {
        closeMenu(false);
      }
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        closeMenu(true);
      }
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 767) {
        closeMenu(false);
      }
    });
  }

  function initLanguageSwitch() {
    var currentPath = window.location.pathname;
    var links = document.querySelectorAll("[data-language-switch]");
    function syncLanguageLinks() {
      var currentHash = window.location.hash || "";
      links.forEach(function (link) {
        var target = link.getAttribute("data-language-switch");
        if (!target) {
          return;
        }
        var nextPath = currentPath.replace(/\/(zh-hans|en)(?=\/|$)/, "/" + target);
        link.setAttribute("href", (nextPath || "/" + target + "/") + currentHash);
      });
    }
    syncLanguageLinks();
    window.addEventListener("hashchange", syncLanguageLinks);
  }

  function initYearLabel() {
    document.querySelectorAll("[data-current-year]").forEach(function (node) {
      node.textContent = String(new Date().getFullYear());
    });
  }

  function initMissingContactWarning() {
    var site = window.SCRIPTPACE_SITE || {};
    if (site.supportEmail) {
      document.querySelectorAll("[data-support-email]").forEach(function (link) {
        link.textContent = site.supportEmail;
        link.setAttribute("href", "mailto:" + site.supportEmail);
      });
      return;
    }
    document.querySelectorAll("[data-support-email]").forEach(function (link) {
      link.textContent = "Support contact will be published before launch";
      link.removeAttribute("href");
      link.setAttribute("aria-disabled", "true");
    });
    document.querySelectorAll("[data-contact-warning]").forEach(function (node) {
      node.hidden = false;
    });
  }

  function initAppStoreLinks() {
    var site = window.SCRIPTPACE_SITE || {};
    document.querySelectorAll("[data-app-store-link]").forEach(function (link) {
      if (site.appStoreURL) {
        link.setAttribute("href", site.appStoreURL);
      }
    });
  }

  function initHeaderScrollState() {
    var header = document.querySelector(".site-header");
    if (!header) {
      return;
    }
    var ticking = false;
    function sync() {
      header.classList.toggle("is-scrolled", window.scrollY > 12);
      ticking = false;
    }
    sync();
    window.addEventListener("scroll", function () {
      if (!ticking) {
        ticking = true;
        window.requestAnimationFrame(sync);
      }
    }, { passive: true });
  }

  function initStageReveal() {
    if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      return;
    }
    if (!("IntersectionObserver" in window)) {
      return;
    }
    var targets = document.querySelectorAll(".teleprompter-proof, .screenshot-story, .recording-feature, .feature-row__visual, .price-card--featured");
    if (!targets.length) {
      return;
    }
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -36px 0px" });

    var viewportHeight = window.innerHeight || 800;
    targets.forEach(function (node) {
      var rect = node.getBoundingClientRect();
      if (rect.top > viewportHeight * 0.92) {
        node.classList.add("stage-reveal");
        observer.observe(node);
      }
    });
  }

  initLocaleRedirect();
  initMobileNavigation();
  initLanguageSwitch();
  initYearLabel();
  initMissingContactWarning();
  initAppStoreLinks();
  initHeaderScrollState();
  initStageReveal();
})();
