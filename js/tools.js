fetch('data/tools.json')
.then(res => res.json())
.then(data => {

const container = document.getElementById("tools-list")

container.innerHTML=""

data.forEach(tool=>{

const card = document.createElement("div")

card.className="tool-card"

card.innerHTML = `

<img src="${tool.logo}">

<h3>${tool.name}</h3>

<p>${tool.description}</p>

<div class="category">${tool.category}</div>

<a class="btn" href="/tools/tool.html?tool=${tool.slug}">
View Tool
</a>

`

<h3>
<a href="tools/${tool.slug}/">
${tool.name}
</a>
</h3>

<p>${tool.description}</p>

<a href="${tool.website}" target="_blank">
Visit Tool
</a>

`

container.appendChild(card)

})

})