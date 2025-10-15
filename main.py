from PIL import Image, ImageOps

bw_image = Image.open("your_image.jpeg").convert("RGB")
wheel_color = Image.open("color_wheel.png").convert("RGB")
wheel_gray = Image.open("color_wheel-modified.png").convert("RGB")


width, height = bw_image.size
w_width, w_height = wheel_color.size


pixels_bwimg = bw_image.load()
pixels_wheel_color = wheel_color.load()
pixels_wheel_gray = wheel_gray.load()


new_img = Image.new("RGB", (width, height))


gray_to_color = {}
for y in range(w_height):
    for x in range(w_width):
        gray = pixels_wheel_gray[x, y]
        if gray not in gray_to_color:  # store first match
            gray_to_color[gray] = pixels_wheel_color[x, y]


for y in range(height):
    for x in range(width):
        pixel = pixels_bwimg[x, y]
        if pixel in gray_to_color:
            new_img.putpixel((x, y), gray_to_color[pixel])
        else:
            new_img.putpixel((x, y), pixel)  # fallback if no match


new_img.save("coloredImage.png")
print("✅ Saved: coloredImage.png")


inverted_img = ImageOps.invert(new_img)
inverted_img.save("coloredImage_inverted.png")
print("✅ Saved: coloredImage_inverted.png")
