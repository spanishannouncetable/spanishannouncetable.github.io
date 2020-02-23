d3.csv("news.csv").then(function(newsData) {
    newsData.forEach(function(data) {
      d3.select('tbody')
        .selectAll('tr')
        .data(newsData)
        .enter()
        .append('tr')
        .html(function(d) {
            return `
            <a href="${d.Link}" target="_blank">
            <div class="media">
                <img src="${d.ImageLink}" class="align-self-center">
                <div class="media-body">
                    <h3>${d.Headline}</h3>
                    <h5>${d.Source} | ${d.Posted}</h5>
                    ${d.Excerpt}
                </div>
            </div>
            </a>
            `;
        })
    });
});
  