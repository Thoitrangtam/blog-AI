import os

BASE="https://yourdomain.com"

urls=[]

for root,dirs,files in os.walk("."):

    if "index.html" in files:

        path=root.replace(".","")

        urls.append(BASE+path+"/")

xml='<?xml version="1.0" encoding="UTF-8"?>\n'
xml+='<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for u in urls:

    xml+=f"<url><loc>{u}</loc></url>\n"

xml+='</urlset>'

open("sitemap.xml","w").write(xml)