import os

folder="blog"

posts=[]

for root,dirs,files in os.walk(folder):

    for f in files:

        if f=="index.html":
            posts.append(os.path.join(root,f))


for p in posts:

    html=open(p).read()

    for target in posts:

        if target!=p:

            slug=target.split("/")[-2]

            html=html.replace(slug,f'<a href="/blog/{slug}/">{slug}</a>',1)

    open(p,"w").write(html)

print("Internal links added")