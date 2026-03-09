import json

tools=json.load(open("data/tools.json"))

comparisons=[]

for i in range(len(tools)-1):

    comparisons.append({

        "slug":f"{tools[i]['slug']}-vs-{tools[i+1]['slug']}",
        "toolA":tools[i]['name'],
        "toolB":tools[i+1]['name']

    })

open("data/comparisons.json","w").write(json.dumps(comparisons,indent=2))