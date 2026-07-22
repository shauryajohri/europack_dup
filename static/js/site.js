document.addEventListener("DOMContentLoaded", () => {
  // Mobile navigation: the hamburger button ships with no listener in the
  // hotlinked theme JS (its expected markup doesn't line up with ours), so
  // this wires it up directly — toggle the slide-down panel, tap-to-open the
  // "Agencies" submenu, close on outside click / link click / resize to desktop.
  const toggleBtn = document.querySelector("#navbarToggle");
  const menuWrap = document.querySelector(".menu-wrap");

  if (toggleBtn && menuWrap) {
    const closeMenu = () => {
      menuWrap.classList.remove("mobile-menu-open");
      toggleBtn.setAttribute("aria-expanded", "false");
      menuWrap.querySelectorAll(".menu-item-has-children.sub-menu-open").forEach((item) => {
        item.classList.remove("sub-menu-open");
      });
    };

    toggleBtn.addEventListener("click", () => {
      const isOpen = menuWrap.classList.toggle("mobile-menu-open");
      toggleBtn.setAttribute("aria-expanded", String(isOpen));
    });

    const dropdownToggle = menuWrap.querySelector(".menu-item-has-children > a.drop-down");
    const dropdownParent = menuWrap.querySelector(".menu-item-has-children");
    if (dropdownToggle && dropdownParent) {
      dropdownToggle.addEventListener("click", (event) => {
        if (window.innerWidth <= 991) {
          event.preventDefault();
          dropdownParent.classList.toggle("sub-menu-open");
        }
      });
    }

    menuWrap.querySelectorAll(".menu-logo a:not(.drop-down)").forEach((link) => {
      link.addEventListener("click", () => closeMenu());
    });

    document.addEventListener("click", (event) => {
      if (window.innerWidth <= 991 && menuWrap.classList.contains("mobile-menu-open") && !menuWrap.contains(event.target) && event.target !== toggleBtn) {
        closeMenu();
      }
    });

    window.addEventListener("resize", () => {
      if (window.innerWidth > 991) closeMenu();
    });
  }

  const heroSection = document.querySelector(".banner3-section");
  const heroBg = document.querySelector("#home3-banner-bg");
  const heroCards = [...document.querySelectorAll(".banner3-section .eg-card3[data-hero-bg]")];

  function setHeroBackground(card) {
    if (!card) return;

    const imageUrl = card.getAttribute("data-hero-bg");
    const backgroundValue = `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("${imageUrl}")`;

    if (heroBg) heroBg.style.backgroundImage = backgroundValue;
    if (heroSection) heroSection.style.backgroundImage = backgroundValue;

    heroCards.forEach((item) => item.classList.toggle("is-active", item === card));
  }

  heroCards.forEach((card) => {
    card.addEventListener("mouseenter", () => setHeroBackground(card));
    card.addEventListener("mouseover", () => setHeroBackground(card));
    card.addEventListener("pointerenter", () => setHeroBackground(card));
    card.addEventListener("focusin", () => setHeroBackground(card));
  });

  setHeroBackground(heroCards.find((card) => card.classList.contains("is-active")) || heroCards[0]);

  // Homepage "Agencies" logo strip: step over one tile at a time instead of
  // a continuous smooth scroll. The track markup is the tile list rendered
  // twice back-to-back (see components/brands.html), so once we've stepped
  // past the first full set we can snap back to 0 with no transition and
  // the loop looks seamless.
  const brandTrack = document.querySelector(".brand-strip-track");
  if (brandTrack) {
    const tiles = [...brandTrack.children];
    const tileCount = tiles.length / 2;
    let index = 0;
    let timer = null;

    function stepSize() {
      const tile = tiles[0];
      const trackStyles = getComputedStyle(brandTrack);
      const gap = parseFloat(trackStyles.columnGap || trackStyles.gap || "0");
      return tile.getBoundingClientRect().width + gap;
    }

    function advance() {
      index += 1;
      brandTrack.style.transition = "transform 0.7s ease";
      brandTrack.style.transform = `translateX(-${stepSize() * index}px)`;

      if (index >= tileCount) {
        window.setTimeout(() => {
          brandTrack.style.transition = "none";
          brandTrack.style.transform = "translateX(0px)";
          index = 0;
        }, 720);
      }
    }

    function start() {
      stop();
      timer = window.setInterval(advance, 2400);
    }

    function stop() {
      if (timer) window.clearInterval(timer);
    }

    brandTrack.addEventListener("mouseenter", stop);
    brandTrack.addEventListener("mouseleave", start);
    window.addEventListener("resize", () => {
      brandTrack.style.transition = "none";
      brandTrack.style.transform = `translateX(-${stepSize() * index}px)`;
    });

    start();
  }
});
