fetch('/data/tools.json')
.then(res=>res.json())
.then(data=>{

const container=document.getElementById("comparison-list")

for(let i=0;i<data.length;i++){

for(let j=i+1;j<data.length;j++){

const a=data[i]
const b=data[j]

const slug=`${a.slug}-vs-${b.slug}`

const el=document.createElement("div")

el.innerHTML=`
<a href="/comparisons/${slug}/">
${a.name} vs ${b.name}
</a>
`

container.appendChild(el)

}

}

})