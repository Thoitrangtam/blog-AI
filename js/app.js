const container=document.getElementById("toolsContainer")
const search=document.getElementById("searchInput")

let tools=[]

function getDomain(url){

return new URL(url).hostname

}

function getLogo(url){

const domain=getDomain(url)

return `https://www.google.com/s2/favicons?domain=${domain}&sz=128`

}

async function loadTools(){

const res=await fetch("data/tools.json")

tools=await res.json()

renderTools(tools)

}

function renderTools(list){

container.innerHTML=""

list.forEach(tool=>{

const card=document.createElement("div")

card.className="tool-card"

card.innerHTML=`

<img src="${getLogo(tool.url)}">

<h3>${tool.name}</h3>

<span class="category">${tool.category}</span>

<div class="rating">⭐ ${tool.rating}</div>

<p>${tool.description}</p>

<a href="tool.html?tool=${tool.slug}" class="detail-btn">Details</a>

<a href="${tool.url}" target="_blank" class="visit-btn">Visit</a>

`

container.appendChild(card)

})

}

search.addEventListener("input",e=>{

const value=e.target.value.toLowerCase()

const filtered=tools.filter(tool=>

tool.name.toLowerCase().includes(value)||
tool.category.toLowerCase().includes(value)

)

renderTools(filtered)

})

loadTools()