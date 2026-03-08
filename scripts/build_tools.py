import os
import json

# lấy đường dẫn root project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# paths
template_path = os.path.join(BASE_DIR, "templates", "tool_template.html")
data_path = os.path.join(BASE_DIR, "data", "ai_tools.json")
tools_dir = os.path.join(BASE_DIR, "tools")

os.makedirs(tools_dir, exist_ok=True)

# load template
with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

# load ai tools data
with open(data_path, "r", encoding="utf-8") as f:
    tools = json.load(f)
print(f"Generated {len(tools)} tool pages")