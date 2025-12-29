import base64
import os

# Get the absolute path to the 'src' folder
# This goes up two levels from src/app_file/base64image.py to reach src/
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
icon_dir = os.path.join(base_dir, 'image')

icons = []

# Verify directory exists before listing
if not os.path.exists(icon_dir):
    print(f"❗ Error: Could not find directory at {icon_dir}")
else:
    # نرتب الملفات بالاسم باش الترتيب يبقى ثابت
    for filename in sorted(os.listdir(icon_dir)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(icon_dir, filename)
            with open(file_path, "rb") as f:
                icons.append(base64.b64encode(f.read()).decode('utf-8'))

    # نعرض ترتيب الصور باش نتأكد
    for i, name in enumerate(sorted(os.listdir(icon_dir))):
        if name.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"Image {i}: {name}")