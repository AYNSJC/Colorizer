from PIL import Image, ImageOps
import os

input_folder = os.path.join("Images", "Input")
output_folder = os.path.join("Images", "Output")
os.makedirs(output_folder, exist_ok=True)


wheel_color = Image.open("color_wheel.png").convert("RGB")
wheel_gray = Image.open("color_wheel-modified.png").convert("RGB")

w_width, w_height = wheel_color.size
pixels_wheel_color = wheel_color.load()
pixels_wheel_gray = wheel_gray.load()


gray_to_color = {}
for y in range(w_height):
    for x in range(w_width):
        gray = pixels_wheel_gray[x, y]
        if gray not in gray_to_color:
            gray_to_color[gray] = pixels_wheel_color[x, y]


for filename in os.listdir(input_folder):
    if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
        continue  # skip non-image files

    # Load image
    bw_image = Image.open(os.path.join(input_folder, filename)).convert("RGB")
    width, height = bw_image.size
    pixels_bwimg = bw_image.load()


    new_img = Image.new("RGB", (width, height))

    # Apply mapping
    for y in range(height):
        for x in range(width):
            pixel = pixels_bwimg[x, y]
            if pixel in gray_to_color:
                new_img.putpixel((x, y), gray_to_color[pixel])
            else:
                new_img.putpixel((x, y), pixel)

    # Save colorized image
    colorized_path = os.path.join(output_folder, f"colored_{filename}")
    new_img.save(colorized_path)

    # Save inverted image
    inverted_img = ImageOps.invert(new_img)
    inverted_path = os.path.join(output_folder, f"inverted_{filename}")
    inverted_img.save(inverted_path)

    print(f"✅ Processed: {filename}")

print("All images processed successfully!")
