document.addEventListener("DOMContentLoaded", () => {
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

  const translate = document.querySelector(".header-translate");
  const translateToggle = document.querySelector(".translate-toggle");

  if (translate && translateToggle) {
    translateToggle.addEventListener("click", () => {
      const isOpen = translate.classList.toggle("is-open");
      translateToggle.setAttribute("aria-expanded", String(isOpen));
    });

    translate.querySelectorAll("[data-lang]").forEach((button) => {
      button.addEventListener("click", () => {
        const targetLanguage = button.getAttribute("data-lang");
        const pageUrl = window.location.href;
        const translateUrl = `https://translate.google.com/translate?sl=auto&tl=${targetLanguage}&u=${encodeURIComponent(pageUrl)}`;
        window.open(translateUrl, "_blank", "noopener");
      });
    });

    document.addEventListener("click", (event) => {
      if (!translate.contains(event.target)) {
        translate.classList.remove("is-open");
        translateToggle.setAttribute("aria-expanded", "false");
      }
    });
  }
});
