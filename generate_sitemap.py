import os

files = os.listdir("posts")

with open("sitemap.xml","w") as f:

    f.write("<urlset>")

    for file in files:

        url = f"https://tamnguyenai.com/posts/{file}"

        f.write(f"<url><loc>{url}</loc></url>")

    f.write("</urlset>")

print("Sitemap generated")