import os
from ai_tools_list import tools

template_start = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Best AI Tools for {topic}</title>
<link rel="stylesheet" href="style.css">
</head>

<body>

<header>
<div class="container">
<a class="logo" href="/">TamNguyen AI Blog</a>
</div>
</header>

<div class="container">

<h1>Best AI Tools for {topic}</h1>
<p>Discover the best AI tools for {topic}.</p>
"""

template_end = """
</div>

<footer>
© 2026 TamNguyenAI.com
</footer>

</body>
</html>
"""

topics = [
"bloggers",
"marketing",
"seo",
"social-media",
"productivity",
"startups"
]

os.makedirs("posts", exist_ok=True)

for topic in topics:

    filename = f"posts/ai-tools-for-{topic}.html"

    content = template_start.format(topic=topic)

    for tool in tools:

        content += f"""
<div class="tool">

<h3>{tool['name']}</h3>

<p>{tool['description']}</p>

<a class="button" href="{tool['url']}" target="_blank">
Try {tool['name']}
</a>

</div>
"""

    content += template_end

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Posts generated successfully")