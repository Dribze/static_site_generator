import os
import shutil

def copy_files_recursive(source_dir_path, dest_dir_path):
	if os.path.exists(dest_dir_path):
		shutil.rmtree(dest_dir_path)
	os.mkdir(dest_dir_path)
	items = os.listdir(source_dir_path)
	for item in items:
		from_path = os.path.join(source_dir_path, item)
		dest_path = os.path.join(dest_dir_path, item)
		if os.path.isfile(from_path):
			shutil.copy(from_path,dest_path)
			print(f"Copied: {from_path} to {dest_path}")
		else:
			copy_files_recursive(from_path, dest_path)

