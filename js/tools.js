const container = document.getElementById("toolsContainer")
const searchInput = document.getElementById("searchInput")

let tools = []

async function loadTools(){

const res = await fetch("/data/tools.json")
tools = await res.json()

renderTools(tools)

}

function renderTools(list){

container.innerHTML = ""

list.forEach(tool=>{

const card = document.createElement("div")
card.className = "tool-card"

card.innerHTML = `

<img src="${tool.logo}" alt="${tool.name}">

<h3>${tool.name}</h3>

<span class="category">${tool.category}</span>

<div class="rating">⭐ ${tool.rating}</div>

<p>${tool.description}</p>

<a href="${tool.affiliate}" target="_blank" class="visit-btn">Visit</a>

<a href="/tool.html?tool=${tool.slug}" class="detail-btn">Details</a>

`

container.appendChild(card)

})

}

searchInput.addEventListener("input", e=>{

const value = e.target.value.toLowerCase()

const filtered = tools.filter(tool =>
tool.name.toLowerCase().includes(value) ||
tool.category.toLowerCase().includes(value)
)

renderTools(filtered)

})

loadTools()