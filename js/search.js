let toolsData=[]

fetch('data/tools.json')
.then(res=>res.json())
.then(data=>{

toolsData=data

const search=document.getElementById("searchBox")

search.addEventListener("input",function(){

const keyword=this.value.toLowerCase()

const filtered=toolsData.filter(tool=>
tool.name.toLowerCase().includes(keyword)
)

renderTools(filtered)

})

renderTools(data)

})

function renderTools(list){

const container=document.getElementById("tools-list")

container.innerHTML=""

list.forEach(tool=>{

const card=document.createElement("div")

card.className="tool-card"

card.innerHTML=`

<h3>
<a href="tools/${tool.slug}/">
${tool.name}
</a>
</h3>

<p>${tool.description}</p>

`

container.appendChild(card)

})

}