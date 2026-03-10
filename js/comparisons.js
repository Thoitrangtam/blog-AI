fetch('data/tools.json')
.then(res=>res.json())
.then(data=>{

const container=document.getElementById("comparison-list")

container.innerHTML=""

for(let i=0;i<data.length;i++){

for(let j=i+1;j<data.length;j++){

const a=data[i]
const b=data[j]

const el=document.createElement("div")

el.className="comparison-card"

el.innerHTML=`
<a href="comparisons/${a.slug}-vs-${b.slug}/">
${a.name} vs ${b.name}
</a>
`

container.appendChild(el)

}

}

})