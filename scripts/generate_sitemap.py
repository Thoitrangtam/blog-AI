import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

folders=["tools","comparisons","posts"]

urls=[]

for folder in folders:

    path=os.path.join(BASE_DIR,folder)

    for file in os.listdir(path):

        if file.endswith(".html"):

            urls.append(f"https://yourdomain.com/{folder}/{file}")

sitemap="<?xml version='1.0' encoding='UTF-8'?>\n<urlset>"

for url in urls:

    sitemap+=f"<url><loc>{url}</loc></url>"

sitemap+="</urlset>"

with open(os.path.join(BASE_DIR,"sitemap.xml"),"w") as f:

    f.write(sitemap)

print("Sitemap generated")