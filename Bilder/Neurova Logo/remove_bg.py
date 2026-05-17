from PIL import Image
import os

def make_transparent(input_path, output_path, target_color=(255, 255, 255), tolerance=30):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # Check if the pixel is close to the target color (white)
        if all(abs(item[i] - target_color[i]) <= tolerance for i in range(3)):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")

logos = [
    ("neurova_main_logo.png", "neurova_main_logo_transparent.png"),
    ("neurova_secondary_logo.png", "neurova_secondary_logo_transparent.png"),
    ("neurova_monochrome.png", "neurova_monochrome_transparent.png"),
    ("neurova_icon.png", "neurova_icon_transparent.png")
]

for input_file, output_file in logos:
    if os.path.exists(input_file):
        make_transparent(input_file, output_file)
        print(f"Created {output_file}")

# Special case for dark mode (black background)
if os.path.exists("neurova_dark_mode.png"):
    make_transparent("neurova_dark_mode.png", "neurova_dark_mode_transparent.png", target_color=(5, 7, 11), tolerance=10)
    print("Created neurova_dark_mode_transparent.png")
