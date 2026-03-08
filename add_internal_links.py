import os
import random

files=os.listdir("posts")

for file in files:

    path=f"posts/{file}"

    with open(path,"r",encoding="utf-8") as f:
        content=f.read()

    links=random.sample(files,min(3,len(files)))

    html="<h2>Related Articles</h2><ul>"

    for link in links:
        if link!=file:
            html+=f"<li><a href='/posts/{link}'>{link}</a></li>"

    html+="</ul>"

    content=content.replace("</footer>",html+"</footer>")

    with open(path,"w",encoding="utf-8") as f:
        f.write(content)

print("Internal links added")