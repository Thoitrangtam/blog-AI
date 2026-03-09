import json

posts=[]
tools=[]
comparisons=[]
categories=["writing","seo","productivity","marketing"]

for i in range(1,1201):

    posts.append({

        "title":f"Best AI Tools Guide {i}",
        "slug":f"best-ai-tools-{i}",
        "content":"Complete guide about AI tools.",
        "category":categories[i%4]

    })

for i in range(1,301):

    tools.append({

        "name":f"AI Tool {i}",
        "slug":f"ai-tool-{i}",
        "description":"Free AI productivity tool"

    })

for i in range(1,300):

    comparisons.append({

        "slug":f"ai-tool-{i}-vs-ai-tool-{i+1}",
        "toolA":f"AI Tool {i}",
        "toolB":f"AI Tool {i+1}"

    })

json.dump(posts,open("data/posts.json","w"),indent=2)
json.dump(tools,open("data/tools.json","w"),indent=2)
json.dump(comparisons,open("data/comparisons.json","w"),indent=2)

print("data generated")