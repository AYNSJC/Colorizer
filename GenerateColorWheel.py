from PIL import Image
import math
import colorsys  # for hsv_to_rgb

size = 512
radius = size // 2
img = Image.new("RGB", (size, size))
pixels = img.load()

for y in range(size):
    for x in range(size):
        dx = x - radius
        dy = y - radius
        dist = math.sqrt(dx * dx + dy * dy)

        if dist <= radius:
            # Angle = hue, distance = saturation
            angle = math.atan2(dy, dx)
            hue = (angle + math.pi) / (2 * math.pi)  # range [0,1)
            sat = dist / radius                       # range [0,1]
            val = 1.0                                 # max brightness

            # Convert HSV -> RGB (colorsys uses 0–1 range)
            r, g, b = colorsys.hsv_to_rgb(hue, sat, val)
            pixels[x, y] = (int(r * 255), int(g * 255), int(b * 255))
        else:
            pixels[x, y] = (255, 255, 255)

img.save("color_wheel.png")
print("✅ Saved color_wheel.png")
