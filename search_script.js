
let articles = [];

 // Fetch articles from JSON
fetch('https://poonh.github.io/travel_blog/articles.json')
  .then(response => {
    console.log('Fetched articles.json:', response);
    return response.json();
  })
  .then(data => {
    console.log('Loaded articles:', data);
    articles = data;
  })
  .catch(error => console.error('Error fetching articles.json:', error));

// Search function
function searchArticles() {
  const query = document.getElementById("search-box").value.toLowerCase().trim();

  // Split query into individual keywords by spaces
  const keywords = query.split(/\s+/);

  const resultsContainer = document.getElementById("search-results");
  resultsContainer.innerHTML = ""; // Clear previous results

  if (keywords.length > 0) {
    const filteredArticles = articles.filter(article => {
      // Check if any of the keywords match the article
      return keywords.some(keyword =>
        article.title.toLowerCase().includes(keyword) ||
        article.description.toLowerCase().includes(keyword) ||
        article.tags.some(tag => tag.toLowerCase().includes(keyword))
      );
    });

    // Display results
    if (filteredArticles.length > 0) {
      filteredArticles.forEach(article => {
        const resultItem = document.createElement("div");
        resultItem.innerHTML = `
          <a href="${article.url}" target="_blank"><h3>${article.title}</h3></a>
          <p>${article.description}</p>
        `;
        resultsContainer.appendChild(resultItem);
      });
    } else {
      resultsContainer.innerHTML = "<p>没有结果</p>";
    }
  }
}

// Add event listener to the "Search" button
document.getElementById("search-button").addEventListener("click", searchArticles);
document.getElementById("search-box").addEventListener("keypress", (event) => {
  if (event.key === "Enter") {
    searchArticles();
  }
});
