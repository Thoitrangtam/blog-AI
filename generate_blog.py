import os

titles = [
"AI Tools for Marketing",
"AI Tools for SEO",
"Best AI Writing Tools",
"AI for Small Business",
"Future of AI Writing"
]

template = """
<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
<meta name="description" content="{title}">
</head>

<body>

<h1>{title}</h1>

<p>Artificial intelligence is transforming the digital world.</p>

<p>Businesses and creators are increasingly using AI tools to improve productivity and create better content.</p>

<h2>Benefits of AI</h2>

<ul>
<li>Automation</li>
<li>Better productivity</li>
<li>Faster content creation</li>
</ul>

</body>
</html>
"""

for title in titles:

    filename = title.lower().replace(" ","-") + ".html"

    with open(filename,"w") as f:
        f.write(template.format(title=title))

print("Blog posts created!")