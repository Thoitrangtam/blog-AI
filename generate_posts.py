import os
import random

# đọc keyword
with open("keywords.txt","r",encoding="utf-8") as f:
    keywords=[k.strip() for k in f.readlines()]

# đọc template
template=open("template.html","r",encoding="utf-8").read()

os.makedirs("posts",exist_ok=True)

created_files=[]

for kw in keywords:

    title=kw.title()

    content=f"""
<h2>Introduction</h2>
<p>{title} are becoming increasingly popular as artificial intelligence grows.</p>

<h2>Benefits of {kw}</h2>
<p>AI tools help automate tasks, improve productivity, and reduce manual work.</p>

<h2>Best {kw}</h2>
<p>There are many AI platforms available that help creators and businesses.</p>

<h2>Conclusion</h2>
<p>{title} will continue to evolve as AI technology improves.</p>
"""

    filename=kw.replace(" ","-")+".html"

    created_files.append(filename)

    html=template.replace("{{title}}",title)
    html=html.replace("{{content}}",content)

    html=html.replace("{{related}}","")

    with open(filename,"w",encoding="utf-8") as f:
        f.write(html)

print("Posts created")