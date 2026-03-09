fetch('/data/tools.json')
.then(res => res.json())
.then(data => {

 let container = document.getElementById("tools-list");

 data.forEach(tool => {

  let card = document.createElement("div");

  card.innerHTML = `
  <h3>
  <a href="/tools/${tool.slug}/">
  ${tool.name}
  </a>
  </h3>

  <p>${tool.description}</p>

  <a href="${tool.website}" target="_blank">
  Visit Tool
  </a>
  `;

  container.appendChild(card);

 });

});