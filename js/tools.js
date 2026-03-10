/* ============================= */
/* GLOBAL DATA */
/* ============================= */

let allTools = []



/* ============================= */
/* LOAD TOOLS FROM JSON */
/* ============================= */

async function loadTools(){

const container =
document.getElementById("tools-container")

if(!container) return

try{

const res =
await fetch("/data/tools.json")

const data =
await res.json()

allTools = data.tools

renderTools(allTools)

}

catch(error){

console.error("Tools load error",error)

container.innerHTML =
"<p>Failed to load tools</p>"

}

}



/* ============================= */
/* RENDER TOOL CARDS */
/* ============================= */

function renderTools(tools){

const container =
document.getElementById("tools-container")

if(!container) return

container.innerHTML=""

tools.forEach(tool=>{

const logo =
`https://logo.clearbit.com/${tool.domain}`

container.innerHTML += `

<div class="tool-card">

<img
src="${logo}"
class="tool-logo"
onerror="this.src='/images/default-logo.png'"
>

<h3>${tool.name}</h3>

<p>${tool.description}</p>

<div class="tool-category">
${tool.category}
</div>

<div class="tool-buttons">

<a href="/tools/tool.html?tool=${tool.slug}"
class="btn-view">

View

</a>

<a href="${tool.affiliate}"
target="_blank"
class="btn-visit">

Visit

</a>

</div>

</div>

`

})

}



/* ============================= */
/* SEARCH TOOLS */
/* ============================= */

function searchTools(){

const input =
document
.getElementById("tool-search")

if(!input) return

const keyword =
input.value.toLowerCase()

const filtered =
allTools.filter(tool=>

tool.name.toLowerCase().includes(keyword) ||

tool.description.toLowerCase().includes(keyword) ||

tool.category.toLowerCase().includes(keyword)

)

renderTools(filtered)

}



/* ============================= */
/* LOAD SINGLE TOOL PAGE */
/* ============================= */

async function loadToolPage(){

const container =
document.getElementById("tool-page")

if(!container) return

const params =
new URLSearchParams(window.location.search)

const slug =
params.get("tool")

if(!slug) return

try{

const res =
await fetch("/data/tools.json")

const data =
await res.json()

const tool =
data.tools.find(t=>t.slug===slug)

if(!tool){

container.innerHTML =
"<p>Tool not found</p>"

return

}

const logo =
`https://logo.clearbit.com/${tool.domain}`

document.title =
tool.name + " | AI Tool"

container.innerHTML = `

<img
src="${logo}"
class="tool-logo"
onerror="this.src='/images/default-logo.png'"
>

<h1>${tool.name}</h1>

<p>${tool.description}</p>

<div class="tool-category">
${tool.category}
</div>

<br>

<a
href="${tool.affiliate}"
target="_blank"
class="btn-view">

Visit ${tool.name}

</a>

`

}

catch(error){

console.error("Tool page error",error)

}

}



/* ============================= */
/* INIT */
/* ============================= */

document.addEventListener("DOMContentLoaded",()=>{

loadTools()

loadToolPage()

})