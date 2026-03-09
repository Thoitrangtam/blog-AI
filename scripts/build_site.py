import os

os.system("python scripts/generate_tools.py")

os.system("python scripts/build_blog.py")

os.system("python scripts/build_categories.py")

os.system("python scripts/generate_comparisons.py")

os.system("python scripts/internal_links.py")

os.system("python scripts/generate_sitemap.py")

print("SITE BUILD COMPLETE")