import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	for filename in os.listdir(dir_path_content):
		from_path = os.path.join(dir_path_content, filename)
		dest_path = os.path.join(dest_dir_path, filename)
		if os.path.isfile(from_path):
			dest_path = Path(dest_path).with_suffix(".html")
			generate_page(from_path, template_path, dest_path)
		else:
			generate_pages_recursive(from_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
	print (f"Generating page from {from_path} to {dest_path} using {template_path}")
	with open(from_path, 'r') as f:
		markdown_content = f.read()
	with open(template_path, 'r') as f:
		template_content = f.read()
	html_node = markdown_to_html_node(markdown_content)
	html_content = html_node.to_html()
	title = extract_title(markdown_content)
	final_html = template_content.replace("{{ Title }}", title)
	final_html = final_html.replace("{{ Content }}", html_content)
	os.makedirs(os.path.dirname(dest_path), exist_ok=True)
	with open(dest_path, 'w') as f:
		f.write(final_html)
def extract_title(markdown):
	lines = markdown.split('\n')
	for line in lines:
		if line.startswith('#'):
			return line[1:].strip()
	raise Exception("no h1 header found in markdown")

