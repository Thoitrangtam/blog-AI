import os
import json
import itertools

# lấy thư mục root của project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "ai_tools.json")
template_path = os.path.join(BASE_DIR, "templates", "comparison_template.html")
output_dir = os.path.join(BASE_DIR, "comparisons")

os.makedirs(output_dir, exist_ok=True)

# load data
with open(data_path, "r", encoding="utf-8") as f:
    tools = json.load(f)

# load template
with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

# tạo các cặp tool để so sánh
for tool1, tool2 in itertools.combinations(tools, 2):

    name1 = tool1["name"]
    name2 = tool2["name"]

    html = template.format(
        tool1=name1,
        tool2=name2,
        description1=tool1["description"],
        description2=tool2["description"]
    )

    filename = f"{name1.lower().replace(' ','-')}-vs-{name2.lower().replace(' ','-')}.html"

    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(html)

print("Comparison pages generated")