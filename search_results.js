// Get the search results from sessionStorage
const searchResults = JSON.parse(sessionStorage.getItem('searchResults'));

// Get the container to display results
const resultsContainer = document.getElementById('search-results');

// Check if there are results
if (searchResults && searchResults.length > 0) {
  searchResults.forEach(article => {
    const resultItem = document.createElement('div');
    resultItem.innerHTML = `
      <a href="${article.url}" target="_blank"><h3>${article.title}</h3></a>
      <p>${article.description}</p>
    `;
    resultsContainer.appendChild(resultItem);
  });
} 
