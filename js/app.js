async function loadTools(){

const res = await fetch('/data/tools.json');

const tools = await res.json();

const grid = document.getElementById('tools-grid');

tools.forEach(tool=>{

const domain = new URL(tool.link).hostname;

const logo = `https://www.google.com/s2/favicons?domain=${domain}&sz=128`;

grid.innerHTML += `

<div class="tool-card">

<img src="${logo}">

<h3>${tool.name}</h3>

<p>${tool.description}</p>

<a href="${tool.link}" target="_blank">Visit</a>

</div>

`;

});

}

loadTools();