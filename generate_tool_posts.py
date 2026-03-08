import json
import os

os.makedirs("tools", exist_ok=True)

with open("ai_tools.json","r",encoding="utf-8") as f:
    tools=json.load(f)

template=open("template.html","r",encoding="utf-8").read()

for tool in tools:

    name=tool["name"]
    category=tool["category"]

    content=f"""
<h2>What is {name}?</h2>
<p>{name} is a popular {category} that uses artificial intelligence to improve productivity and creativity.</p>

<h2>Key Features</h2>
<ul>
<li>AI-powered automation</li>
<li>Easy to use interface</li>
<li>Cloud based platform</li>
</ul>

<h2>Pros</h2>
<ul>
<li>Fast results</li>
<li>Improves productivity</li>
<li>Modern AI technology</li>
</ul>

<h2>Cons</h2>
<ul>
<li>May require subscription</li>
<li>Learning curve for beginners</li>
</ul>

<h2>Conclusion</h2>
<p>{name} is one of the most interesting AI tools in the {category} category.</p>
"""

    title=f"{name} Review – Features, Pros & Cons"

    html=template.replace("{{title}}",title)
    html=html.replace("{{content}}",content)

    filename=f"tools/{name.lower().replace(' ','-')}.html"

    with open(filename,"w",encoding="utf-8") as f:
        f.write(html)

print("Tool pages created!")