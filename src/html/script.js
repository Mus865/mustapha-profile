document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".menu-toggle");
  const navLinks = document.querySelector(".nav-links");

  toggle.addEventListener("click", () => {
    navLinks.classList.toggle("show");

    // Toggle icon between ☰ and ✖
    toggle.textContent = navLinks.classList.contains("show") ? "✖" : "☰";
  });
});

