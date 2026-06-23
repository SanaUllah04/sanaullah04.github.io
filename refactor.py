import re

def refactor_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # We want to replace the sections in Projects, Certificates, Highlights, Experience
    
    # 1. Provide a wrap for year blocks.
    # We can use regex to find sections. But regex might be messy.
    # What if we just target the `<br>` and `<hr>` between items and remove them, and wrap items in `<div class="grid-card">`?
    
    # Actually, let's write a small generic parser since HTML is a bit unstructured.
    # A project has:
    # <div style="text-align: center;">...<a>...</a>...</div>
    # <br>
    # <div style="text-align: center;">...<img...>...</div>
    # <hr>
    
    # Let's clean up all <hr> tags inside <p> inside articles
    pass
