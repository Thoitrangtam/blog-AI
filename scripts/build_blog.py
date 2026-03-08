import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR,"data","ai_tools.json")
posts_dir = os.path.join(BASE_DIR,"posts")

os.makedirs(posts_dir,exist_ok=True)

with open(data_path,"r",encoding="utf-8") as f:
    tools=json.load(f)

for tool in tools:

    name=tool["name"]

    html=f"""
    <html>
    <head>
    <title>{name} Review</title>
    </head>

    <body>

    <h1>{name} Review</h1>

    <p>{tool["description"]}</p>

    <h2>Features</h2>
    <p>{name} offers powerful AI capabilities.</p>

    <h2>Pros</h2>
    <ul>
    <li>Easy to use</li>
    <li>Powerful AI</li>
    </ul>

    <h2>Cons</h2>
    <ul>
    <li>Free plan limited</li>
    </ul>

    </body>
    </html>
    """

    filename=name.lower().replace(" ","-")+".html"

    with open(os.path.join(posts_dir,filename),"w",encoding="utf-8") as f:
        f.write(html)

print("Blog posts generated")