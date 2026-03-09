import os

blog_dir = "blog"

posts = []

for folder in os.listdir(blog_dir):

    path = os.path.join(blog_dir, folder, "index.html")

    if os.path.exists(path):
        posts.append(folder)

for slug in posts:

    path = f"blog/{slug}/index.html"

    with open(path,"r",encoding="utf-8") as f:
        html = f.read()

    links = "<h3>Related Articles</h3><ul>"

    for other in posts[:5]:

        if other != slug:

            links += f'<li><a href="/blog/{other}/">{other.replace("-"," ").title()}</a></li>'

    links += "</ul>"

    html = html.replace("</article>", links + "</article>")

    with open(path,"w",encoding="utf-8") as f:
        f.write(html)

print("Internal links added")