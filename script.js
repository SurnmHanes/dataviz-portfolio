fetch('posts.json')
  .then(response => response.json())
  .then(posts => {
    const container = document.getElementById('blog-posts');

    // Optional: sort posts by date (latest last)
    posts.sort((a, b) => new Date(a.date) - new Date(b.date));

    posts.forEach(post => {
      const article = document.createElement('article');
      article.innerHTML = `
        <h2>${post.title}</h2>
        <time datetime="${post.date}">${new Date(post.date).toDateString()}</time>
        <p>${post.content}</p>
      `;
      container.appendChild(article);
    });
  })
  .catch(err => {
    document.getElementById('blog-posts').innerHTML = "<p>Failed to load blog posts.</p>";
    console.error("Error loading posts:", err);
  });
