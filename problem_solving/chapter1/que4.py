# import os

# path = "/cwh python"
# try:
#     contents = os.listdir(path)
#     for name in contents:
#         print(name)
# except FileNotFoundError:
#     print(f"Directory not found: {path}")
# except PermissionError:
#     print(f"Permission denied to access: {path}")
# except OSError as e:
#     print(f"Error: {e}")
import os

start_path = "/"
for dirpath, dirnames, filenames in os.walk(start_path):
    print("Directory:", dirpath)
    for f in filenames:
        print("  File:", f)
