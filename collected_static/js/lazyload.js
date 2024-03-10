document.addEventListener("DOMContentLoaded", function () {
  const lazyImages = document.querySelectorAll(".lazy");
  const lazyLoad = function () {
    lazyImages.forEach(function (img) {
      if (
        img.getBoundingClientRect().top <= window.innerHeight &&
        img.getBoundingClientRect().bottom >= 0 &&
        getComputedStyle(img).display !== "none"
      ) {
        img.src = img.dataset.src;
        img.classList.remove("lazy");
      }
    });
  };

  // Initial load
  lazyLoad();

  // Load additional images on scroll
  window.addEventListener("scroll", lazyLoad);
});
