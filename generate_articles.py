import os

with open("template.html","r",encoding="utf-8") as f:
    template = f.read()

with open("keywords.txt","r",encoding="utf-8") as f:
    keywords = f.readlines()

for kw in keywords:

    keyword = kw.strip()

    title = keyword.title()

    description = f"Discover the best {keyword} and how AI tools can improve productivity."

    intro = f"In this guide we explore the best {keyword} available today."

    article = template.replace("{{TITLE}}",title)
    article = article.replace("{{DESCRIPTION}}",description)
    article = article.replace("{{INTRO}}",intro)
    article = article.replace("{{KEYWORD}}",keyword)

    filename = keyword.replace(" ","-") + ".html"

    with open(filename,"w",encoding="utf-8") as f:
        f.write(article)

print("Articles generated successfully!")