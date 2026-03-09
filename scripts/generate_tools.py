import json

tools=[]

for i in range(1,51):

    tools.append({

        "name":f"AI Tool {i}",
        "slug":f"ai-tool-{i}",
        "description":"Free AI productivity tool"

    })

open("data/tools.json","w").write(json.dumps(tools,indent=2))

print("Tools generated")