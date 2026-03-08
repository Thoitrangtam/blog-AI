import os
import json
import random

with open("data/ai_tools.json","r") as f:
    tools=json.load(f)

topics=[

"SEO",
"Blogging",
"Marketing",
"Productivity",
"Social Media",
"Ecommerce",
"Content Creation"

]

template=open("templates/post_template.html").read()

os.makedirs("posts",exist_ok=True)

for topic in topics:

    title=f"Best AI Tools For {topic}"

    intro=f"In this guide we explore the best AI tools for {topic}."

    benefits="AI tools help automate tasks and improve productivity."

    conclusion=f"Using AI tools for {topic} can save time and increase efficiency."

    selected=random.sample(tools,3)

    tools_html=""

    for tool in selected:

        tools_html+=f"""
        <div class='tool-card'>
        <h3>{tool['name']}</h3>
        <p>{tool['description']}</p>
        <a href='{tool['url']}' target='_blank'>
        <button>Try {tool['name']}</button>
        </a>
        </div>
        """

    related="""
<ul>
<li><a href="/posts/ai-tools-for-seo.html">AI Tools for SEO</a></li>
<li><a href="/posts/ai-tools-for-blogging.html">AI Tools for Blogging</a></li>
<li><a href="/posts/ai-tools-for-marketing.html">AI Tools for Marketing</a></li>
</ul>
"""

    html=template.replace("{{title}}",title)
    html=html.replace("{{topic}}",topic)
    html=html.replace("{{intro}}",intro)
    html=html.replace("{{benefits}}",benefits)
    html=html.replace("{{conclusion}}",conclusion)
    html=html.replace("{{tools}}",tools_html)
    html=html.replace("{{related}}",related)

    filename=topic.lower().replace(" ","-")

    with open(f"posts/ai-tools-for-{filename}.html","w",encoding="utf-8") as f:
        f.write(html)

print("Posts generated successfully")