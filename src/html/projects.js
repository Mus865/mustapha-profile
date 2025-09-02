const username = "Mus865";
const projectsContainer = document.getElementById("projects");

fetch(`https://api.github.com/users/${username}/repos?per_page=100`)
  .then(response => response.json())
  .then(repos => {
    // Sort by most recently updated
    repos.sort((a, b) => new Date(b.updated_at) - new Date(a.updated_at));

    repos.forEach((repo, index) => {
      const card = document.createElement("div");
      card.className = "project-card";
      card.innerHTML = `
        <h2>${index + 1}. ${repo.name}</h2>
        <p>${repo.description || "No description provided."}</p>
        <a href="${repo.html_url}" target="_blank">View on GitHub</a>
      `;
      projectsContainer.appendChild(card);

      // Scroll animation (if you're using it)
      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1 });

      observer.observe(card);
    });
  })
  .catch(error => {
    projectsContainer.innerHTML = "<p>Failed to load projects. Please try again later.</p>";
    console.error("GitHub API error:", error);
  });

  // Existing GitHub fetch logic...
// After appending each card:
projectsContainer.appendChild(card);

// Observe visibility
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

// Apply observer to each card
observer.observe(card);
