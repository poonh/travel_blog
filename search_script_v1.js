
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
   const query = document.getElementById("search-box").value.toLowerCase();
   const resultsContainer = document.getElementById("search-results");
   resultsContainer.innerHTML = ""; // Clear previous results

   if (query) {
     const filteredArticles = articles.filter(article =>
       article.title.toLowerCase().includes(query) ||
       article.description.toLowerCase().includes(query) ||
       article.tags.some(tag => tag.toLowerCase().includes(query))
     );

     // Display results
     filteredArticles.forEach(article => {
       const resultItem = document.createElement("div");
       resultItem.innerHTML = `
         <a href="${article.url}" target="_blank"><h3>${article.title}</h3></a>
         <p>${article.description}</p>
       `;
       resultsContainer.appendChild(resultItem);
     });
   }
 }

 // Add event listener to the "Search" button
 document.getElementById("search-button").addEventListener("click", searchArticles);
document.getElementById("search-box").addEventListener("keypress", (event) => {
  if (event.key === "Enter") {
    searchArticles();
  }
});

