import os

search_path = 'work'

for path, sub_dirs, files in os.walk(search_path):
    print(f"Searching: {path}")
    print(f"\tFolders: {sub_dirs}")
    print(f"\tFiles: {files}\n")
