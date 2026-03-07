import os

domain = "https://tamnguyenai.com"

html_files = [f for f in os.listdir() if f.endswith(".html")]

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for file in html_files:

    url = f"{domain}/{file}"

    sitemap += "  <url>\n"
    sitemap += f"    <loc>{url}</loc>\n"
    sitemap += "  </url>\n"

sitemap += "</urlset>"

with open("sitemap.xml","w",encoding="utf-8") as f:
    f.write(sitemap)

print("Sitemap generated!")