import json
import os

with open("data/ai_tools.json") as f:
    tools=json.load(f)

template=open("templates/tool_template.html").read()

os.makedirs("tools",exist_ok=True)

for tool in tools:

    features="".join([f"<li>{f}</li>" for f in tool["features"]])
    pros="".join([f"<li>{p}</li>" for p in tool["pros"]])
    cons="".join([f"<li>{c}</li>" for c in tool["cons"]])
    alternatives="".join([f"<li>{a}</li>" for a in tool.get("alternatives",[])])

    html=template.replace("{{tool_name}}",tool["name"])
    html=html.replace("{{description}}",tool["description"])
    html=html.replace("{{features}}","<ul>"+features+"</ul>")
    html=html.replace("{{pros}}","<ul>"+pros+"</ul>")
    html=html.replace("{{cons}}","<ul>"+cons+"</ul>")
    html=html.replace("{{pricing}}",tool["pricing"])
    html=html.replace("{{best_for}}",tool["best_for"])
    html=html.replace("{{alternatives}}","<ul>"+alternatives+"</ul>")
    html=html.replace("{{url}}",tool["url"])

    filename=tool["name"].lower().replace(" ","-")

    with open(f"tools/{filename}.html","w",encoding="utf-8") as f:
        f.write(html)

print("Tool pages generated")