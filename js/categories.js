async function loadCategories(){

const res=await fetch("data/categories.json")

const cats=await res.json()

const div=document.getElementById("categories")

cats.forEach(c=>{

div.innerHTML+=`<a class="category-link" href="/?search=${c.slug}">${c.name}</a>`

})

}

loadCategories()