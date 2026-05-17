from PIL import Image
import os

def make_transparent(input_path, output_path, target_color=(255, 255, 255), tolerance=30):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        if all(abs(item[i] - target_color[i]) <= tolerance for i in range(3)):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")

logos = [
    ("neurova_main_logo_v3.png", "neurova_main_logo_v3_transparent.png"),
    ("neurova_icon_v3.png", "neurova_icon_v3_transparent.png"),
    ("neurova_monochrome_v3.png", "neurova_monochrome_v3_transparent.png")
]

for input_file, output_file in logos:
    if os.path.exists(input_file):
        make_transparent(input_file, output_file)
        print(f"Created {output_file}")

if os.path.exists("neurova_dark_mode_v3.png"):
    make_transparent("neurova_dark_mode_v3.png", "neurova_dark_mode_v3_transparent.png", target_color=(0, 0, 0), tolerance=15)
    print("Created neurova_dark_mode_v3_transparent.png")
