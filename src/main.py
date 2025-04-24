import sys
from gencontent import generate_page
from textnode import TextNode, TextType
from gencontent import generate_pages_recursive
import os
import shutil
from copystatic import copy_files_recursive
dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"
def main():
	basepath = default_basepath
	if len(sys.argv) > 1:
		basepath = sys.argv[1]
	print("deleting public directory....")
	print("copying files from static to public directory...")
	copy_files_recursive(dir_path_static, dir_path_public)
	print("generating page...")
	generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)





if __name__ == "__main__":
    main()

