import json

posts = []

for i in range(1,201):

    posts.append({
        "title": f"Best AI Tools for Task {i}",
        "slug": f"best-ai-tools-{i}",
        "content": f"<p>Guide about AI tools {i}</p>"
    })

open("data/posts.json","w").write(json.dumps(posts,indent=2))

print("200 blog posts generated")