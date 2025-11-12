import os, base64, re

def combine_allure_to_single_html(allure_dir, output_html):
    index_path = os.path.join(allure_dir, "index.html")

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace <script src="..."></script> with inline content
    def inline_script(match):
        src = match.group(1)
        js_path = os.path.join(allure_dir, src)
        if os.path.exists(js_path):
            with open(js_path, "r", encoding="utf-8", errors="ignore") as js_file:
                js_content = js_file.read()
            return f"<script>{js_content}</script>"
        return ""

    html = re.sub(r'<script src="([^"]+)"></script>', inline_script, html)

    # Replace <link href="...css"> with inline <style>
    def inline_css(match):
        href = match.group(1)
        css_path = os.path.join(allure_dir, href)
        if os.path.exists(css_path):
            with open(css_path, "r", encoding="utf-8", errors="ignore") as css_file:
                css_content = css_file.read()
            return f"<style>{css_content}</style>"
        return ""

    html = re.sub(r'<link href="([^"]+)" rel="stylesheet"[^>]*>', inline_css, html)

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Combined Allure report created: {output_html}")

if __name__ == "__main__":
    combine_allure_to_single_html("allure-report", "allure-report-single.html")
