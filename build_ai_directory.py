import json
import os

os.makedirs("tools", exist_ok=True)

template=open("template.html","r",encoding="utf-8").read()

with open("ai_tools.json","r",encoding="utf-8") as f:
    tools=json.load(f)

for tool in tools:

    name=tool["name"]
    category=tool["category"]
    description=tool["description"]
    website=tool["website"]

    content=f"""
<h2>What is {name}?</h2>
<p>{description}</p>

<h2>Category</h2>
<p>{category}</p>

<h2>Main Features</h2>
<ul>
<li>AI automation</li>
<li>Cloud platform</li>
<li>Easy to use</li>
</ul>

<h2>Pros</h2>
<ul>
<li>Fast and powerful AI</li>
<li>Useful for productivity</li>
</ul>

<h2>Cons</h2>
<ul>
<li>Some features require subscription</li>
</ul>

<h2>Official Website</h2>
<p><a href="{website}">{name} Official Website</a></p>
"""

    title=f"{name} Review – Features, Pros, Pricing"

    html=template.replace("{{title}}",title)
    html=html.replace("{{content}}",content)

    filename=f"tools/{name.lower().replace(' ','-')}.html"

    with open(filename,"w",encoding="utf-8") as f:
        f.write(html)

print("AI tool pages generated")