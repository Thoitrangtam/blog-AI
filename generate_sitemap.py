import os

base_url="https://tamnguyenai.com"

files=os.listdir("posts")

with open("sitemap.xml","w",encoding="utf-8") as f:

    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

    for file in files:

        url=base_url+"/posts/"+file

        f.write("<url>\n")
        f.write(f"<loc>{url}</loc>\n")
        f.write("</url>\n")

    f.write("</urlset>")

print("Sitemap created!")