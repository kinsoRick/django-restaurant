// favorites.js

document.addEventListener("DOMContentLoaded", () => {
  refreshLikedNotification();

  const search = document.querySelector("#search-input-navbar");
  const searchDismiss = document.querySelector("#search-input-dismiss");
  const searchOpen = document.querySelector("#search-open");

  searchDismiss.addEventListener("click", (event) => {
    event.preventDefault();
    document.querySelector(".search-form").classList.remove("active")
    document.querySelector(".header-navbar").classList.remove("search-active");
  })

  searchOpen.addEventListener("click", (event) => {
    event.preventDefault();
    document.querySelector(".search-form").classList.add("active")
    document.querySelector(".header-navbar").classList.add("search-active");
  })

  const debouncedUpdateQuery = debounce(updateQuery, 300);
  search.addEventListener("input", debouncedUpdateQuery);

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();

      const targetId = this.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);

      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop + 340,  // Adjust the offset as needed
          behavior: 'smooth'
        });
      }
    });
  });

  document.querySelector(".logo").addEventListener("click", (e) => {
    if (!e.target.classList.contains("logo")) return;
    window.location.href = (RESTAURANT) ? `${window.location.origin}/restaurant` : `${window.location.origin}/`;
  })
});

document.addEventListener("DOMContentLoaded", () => {
  const favoriteModalElement = document.querySelector("#favoriteModal");

  favoriteModalElement.addEventListener("shown.bs.modal", async () => {
    const body = favoriteModalElement.querySelector(".modal-body");

    await refreshBody(body)
  })
});
