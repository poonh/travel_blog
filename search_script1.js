
let articles = [];

 // Fetch articles from JSON
fetch('https://poonh.github.io/travel_blog/articles1.json')
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
  const query = document.getElementById("search-box").value.toLowerCase();
  
  // Filter articles based on the query
  const filteredArticles = articles.filter(article =>
    article.title.toLowerCase().includes(query) ||
    article.description.toLowerCase().includes(query) ||
    article.tags.some(tag => tag.toLowerCase().includes(query))
  );

  // If there are results, open the results page and pass the data
  if (filteredArticles.length > 0) {
    // Store search results in sessionStorage (this is temporary data for the session)
    sessionStorage.setItem('searchResults', JSON.stringify(filteredArticles));

    // Open a new tab with the search results
    window.open('search_results.html', '_blank');
  } else {
    alert('没有结果');
  }
}

// Add event listener to the "Search" button
document.getElementById("search-button").addEventListener("click", searchArticles);
document.getElementById("search-box").addEventListener("keypress", (event) => {
  if (event.key === "Enter") {
    searchArticles();
  }
});
