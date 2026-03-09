import json
import itertools

tools = json.load(open("data/tools.json"))

pairs = itertools.combinations(tools,2)

for a,b in pairs:

 slug = f"{a['slug']}-vs-{b['slug']}"

 print(slug)