import os

print("Generating articles...")
os.system("python generate_articles.py")

print("Adding internal links...")
os.system("python add_internal_links.py")

print("Generating sitemap...")
os.system("python generate_sitemap.py")

print("Committing changes...")
os.system("git add .")
os.system('git commit -m "auto update articles"')

print("Pushing to GitHub...")
os.system("git push")

print("Done! Website updated.")