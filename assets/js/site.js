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

  initLocaleRedirect();
  initMobileNavigation();
  initLanguageSwitch();
  initYearLabel();
  initMissingContactWarning();
  initAppStoreLinks();
})();
