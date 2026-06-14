(function () {
  /* ---- Language menu ---- */
  const languageMenu = document.querySelector(".language-menu");
  const languageButton = document.querySelector(".language-button");
  const languageDropdown = document.querySelector(".language-dropdown");

  function closeMenu() {
    if (!languageMenu || !languageButton) return;
    languageMenu.classList.remove("open");
    languageButton.setAttribute("aria-expanded", "false");
  }

  if (languageButton && languageDropdown) {
    languageButton.addEventListener("click", function (event) {
      event.stopPropagation();
      const isOpen = languageMenu.classList.toggle("open");
      languageButton.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });

    document.addEventListener("click", function (event) {
      if (!languageMenu.contains(event.target)) closeMenu();
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") closeMenu();
    });
  }

  /* ---- Screenshot carousel ---- */
  const slides = Array.from(document.querySelectorAll(".carousel-slide"));
  const dotsWrap = document.querySelector(".carousel-dots");
  const prevBtn = document.querySelector(".carousel-btn.prev");
  const nextBtn = document.querySelector(".carousel-btn.next");
  let current = 0;

  function showSlide(index) {
    if (!slides.length) return;
    current = (index + slides.length) % slides.length;
    slides.forEach(function (slide, i) {
      slide.classList.toggle("active", i === current);
    });
    if (dotsWrap) {
      dotsWrap.querySelectorAll("button").forEach(function (dot, i) {
        dot.classList.toggle("active", i === current);
      });
    }
  }

  if (slides.length && dotsWrap) {
    slides.forEach(function (_, i) {
      const dot = document.createElement("button");
      dot.type = "button";
      dot.setAttribute("aria-label", "Slide " + (i + 1));
      dot.addEventListener("click", function () { showSlide(i); });
      dotsWrap.appendChild(dot);
    });
    showSlide(0);
  }

  if (prevBtn) prevBtn.addEventListener("click", function () { showSlide(current - 1); });
  if (nextBtn) nextBtn.addEventListener("click", function () { showSlide(current + 1); });
})();
