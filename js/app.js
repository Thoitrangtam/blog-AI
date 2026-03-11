async function loadTools() {

const res = await fetch('/data/tools.json');
const tools = await res.json();

const container = document.getElementById('tools-grid');

tools.forEach(tool => {

const domain = new URL(tool.link).hostname;

const logo = `https://www.google.com/s2/favicons?domain=${domain}&sz=128`;

const card = `
<div class="tool-card">

<img src="${logo}" alt="${tool.name}">

<h3>${tool.name}</h3>

<p>${tool.description}</p>

<a href="/tool.html?name=${tool.name}">View Tool</a>

</div>
`;

container.innerHTML += card;

});

}

loadTools();