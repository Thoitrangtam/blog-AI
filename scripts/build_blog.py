import os
import json

# Load template
with open("templates/post_template.html", "r", encoding="utf-8") as f:
    template = f.read()

# Load header
with open("includes/header.html", "r", encoding="utf-8") as f:
    header = f.read()

# Load footer
with open("includes/footer.html", "r", encoding="utf-8") as f:
    footer = f.read()

# Load blog data
with open("data/blog_posts.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

for post in posts:

    title = post["title"]
    slug = post["slug"]
    content = post["content"]
    description = post["description"]

    html = template

    html = html.replace("{{title}}", title)
    html = html.replace("{{content}}", content)
    html = html.replace("{{description}}", description)
    html = html.replace("{{header}}", header)
    html = html.replace("{{footer}}", footer)

    folder = f"blog/{slug}"

    os.makedirs(folder, exist_ok=True)

    with open(f"{folder}/index.html", "w", encoding="utf-8") as f:
        f.write(html)

print("Blog pages created!")