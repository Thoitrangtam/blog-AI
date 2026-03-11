function getLogo(url){

const domain=new URL(url).hostname

return `https://www.google.com/s2/favicons?domain=${domain}&sz=128`

}

async function loadTool(){

const params=new URLSearchParams(location.search)

const slug=params.get("tool")

const res=await fetch("data/tools.json")

const tools=await res.json()

const tool=tools.find(t=>t.slug===slug)

document.getElementById("logo").src=getLogo(tool.url)

document.getElementById("name").innerText=tool.name

document.getElementById("desc").innerText=tool.description

document.getElementById("rating").innerText="⭐ "+tool.rating

document.getElementById("visit").href=tool.url

}

loadTool()