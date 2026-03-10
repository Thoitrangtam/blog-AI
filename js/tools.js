let allTools = [];

async function loadTools() {

const container = document.getElementById("tools-container");

if (!container) return;

try {

const res = await fetch("data/tools.json");
const data = await res.json();

allTools = data.tools;

renderTools(allTools);

} catch (error) {

console.error("Error loading tools:", error);

}

}

function renderTools(tools) {

const container = document.getElementById("tools-container");

container.innerHTML = "";

tools.forEach(tool => {

const logo = "https://www.google.com/s2/favicons?sz=128&domain=" + tool.domain;

container.innerHTML += `

<div class="tool-card">

<img src="${logo}" class="tool-logo">

<h3>${tool.name}</h3>

<p>${tool.description}</p>

<div class="tool-buttons">

<a href="${tool.affiliate}" target="_blank" class="btn-visit">Visit</a>

</div>

</div>

`;

});

}

function searchTools() {

const keyword = document.getElementById("tool-search").value.toLowerCase();

const filtered = allTools.filter(tool =>

tool.name.toLowerCase().includes(keyword) ||
tool.description.toLowerCase().includes(keyword)

);

renderTools(filtered);

}

document.addEventListener("DOMContentLoaded", loadTools);