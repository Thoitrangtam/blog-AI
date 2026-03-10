async function loadTools(){

const res = await fetch("/data/tools.json")
const tools = await res.json()

const container = document.getElementById("tools-container")

if(!container) return

tools.forEach(tool => {

const card = document.createElement("div")
card.className = "tool-card"

card.innerHTML = `

<a href="/tools/tool.html?tool=${tool.slug}">

<img src="${tool.logo}" width="40">

<h3>${tool.name}</h3>

<p>${tool.description}</p>

<span>${tool.category}</span>

</a>

`

container.appendChild(card)

})

}

async function loadToolPage(){

const params = new URLSearchParams(window.location.search)
const slug = params.get("tool")

if(!slug) return

const res = await fetch("/data/tools.json")
const tools = await res.json()

const tool = tools.find(t => t.slug === slug)

if(!tool){

document.body.innerHTML = "Tool not found"
return

}

document.getElementById("tool-name").innerText = tool.name
document.getElementById("tool-description").innerText = tool.description
document.getElementById("tool-logo").src = tool.logo
document.getElementById("tool-link").href = tool.website
document.getElementById("tool-category").innerText = tool.category

}

window.addEventListener("DOMContentLoaded", () => {

loadTools()
loadToolPage()

})
