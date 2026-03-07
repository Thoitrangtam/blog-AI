import os
import random

html_files = [f for f in os.listdir() if f.endswith(".html")]

for file in html_files:

    with open(file,"r",encoding="utf-8") as f:
        content = f.read()

    others = [x for x in html_files if x != file]

    related = random.sample(others, min(4,len(others)))

    links = "<h2>Related Articles</h2>\n<ul>\n"

    for r in related:

        title = r.replace(".html","").replace("-"," ").title()

        links += f'<li><a href="/{r}">{title}</a></li>\n'

    links += "</ul>"

    content = content.replace("</footer>",links+"\n</footer>")

    with open(file,"w",encoding="utf-8") as f:
        f.write(content)

print("Internal links added!")