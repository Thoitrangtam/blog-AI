import os
import random

folder = "posts"

files = os.listdir(folder)

for file in files:

    path = os.path.join(folder, file)

    with open(path,"r",encoding="utf-8") as f:
        content = f.read()

    links = random.sample(files, min(3,len(files)))

    links_html = "<h2>Related Articles</h2><ul>"

    for link in links:

        if link != file:
            url = link.replace(".html","")
            links_html += f'<li><a href="/posts/{link}">{url}</a></li>'

    links_html += "</ul>"

    content = content.replace("</footer>", links_html + "</footer>")

    with open(path,"w",encoding="utf-8") as f:
        f.write(content)

print("Internal links added")