import os
import random
from ai_tools_list import tools

topics = [
"SEO",
"Blogging",
"Marketing",
"Social Media",
"Productivity",
"Startups",
"Content Creation"
]

template = open("templates/post_template.html").read()

os.makedirs("posts", exist_ok=True)

for topic in topics:

    title = f"Best AI Tools For {topic}"

    intro = f"In this guide we explore the best AI tools for {topic}."

    benefits = "AI tools help automate tasks and increase productivity."

    conclusion = f"Using AI tools for {topic} can save time and improve results."

    selected = random.sample(tools,3)

    tools_html = ""

    for tool in selected:

        tools_html += f"""
        <div class='tool-card'>
        <h3>{tool['name']}</h3>
        <p>{tool['description']}</p>
        <a href='{tool['url']}' target='_blank'>
        <button>Try {tool['name']}</button>
        </a>
        </div>
        """

    html = template.replace("{{title}}",title)
    html = html.replace("{{intro}}",intro)
    html = html.replace("{{benefits}}",benefits)
    html = html.replace("{{conclusion}}",conclusion)
    html = html.replace("{{tools}}",tools_html)

    filename = topic.lower().replace(" ","-")

    with open(f"posts/ai-tools-for-{filename}.html","w",encoding="utf-8") as f:
        f.write(html)

print("Posts generated successfully")