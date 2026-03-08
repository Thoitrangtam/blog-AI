import json
import os
import random

with open("ai_tools.json","r",encoding="utf-8") as f:
    tools=json.load(f)

topics=[
"best ai tools for business",
"best ai tools for students",
"ai tools for content creators",
"ai tools for marketing",
"top ai productivity tools"
]

template=open("templates/post_template.html","r",encoding="utf-8").read()

os.makedirs("posts",exist_ok=True)

for topic in topics:

    selected=random.sample(tools,min(3,len(tools)))

    tools_html=""

    for tool in selected:

        pros="<li>"+"</li><li>".join(tool["pros"])+"</li>"
        cons="<li>"+"</li><li>".join(tool["cons"])+"</li>"

        tools_html+=f"""
        <h2>{tool["name"]}</h2>
        <p>Category: {tool["category"]}</p>

        <h3>Pros</h3>
        <ul>{pros}</ul>

        <h3>Cons</h3>
        <ul>{cons}</ul>
        """

    html=template.replace("{{title}}",topic.title())
    html=html.replace("{{content}}",tools_html)

    filename=f"posts/{topic.replace(' ','-')}.html"

    with open(filename,"w",encoding="utf-8") as f:
        f.write(html)

print("Posts generated!")