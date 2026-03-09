import json
import os

BASE=open("templates/base.html").read()
HEADER=open("includes/header.html").read()
FOOTER=open("includes/footer.html").read()

posts=json.load(open("data/posts.json"))
tools=json.load(open("data/tools.json"))
comparisons=json.load(open("data/comparisons.json"))

def render(title,desc,content):

    html=BASE

    html=html.replace("{{header}}",HEADER)
    html=html.replace("{{footer}}",FOOTER)

    html=html.replace("{{title}}",title)
    html=html.replace("{{description}}",desc)
    html=html.replace("{{content}}",content)

    return html


def save(path,html):

    os.makedirs(path,exist_ok=True)

    open(f"{path}/index.html","w",encoding="utf8").write(html)


for p in posts:

    content=f"<h1>{p['title']}</h1><p>{p['content']}</p>"

    html=render(p["title"],p["title"],content)

    save(f"blog/{p['slug']}",html)


for t in tools:

    content=f"<h1>{t['name']}</h1><p>{t['description']}</p>"

    html=render(t["name"],t["description"],content)

    save(f"tools/{t['slug']}",html)


for c in comparisons:

    content=f"<h1>{c['toolA']} vs {c['toolB']}</h1>"

    html=render(content,content,content)

    save(f"comparisons/{c['slug']}",html)


print("site built")