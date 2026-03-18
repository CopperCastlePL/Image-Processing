from PIL import Image
import math

img = Image.open("potworek_pixelart.png").convert("RGB")
width, height = img.size

scale = 10
new_width = width * scale
new_height = height * scale

result = Image.new("RGB", (new_width, new_height))

for y in range(new_height):
    for x in range(new_width):

        src_x = x / scale
        src_y = y / scale

        x1 = int(math.floor(src_x))
        y1 = int(math.floor(src_y))

        x2 = min(x1 + 1, width - 1)
        y2 = min(y1 + 1, height - 1)

        p1 = img.getpixel((x1, y1))
        p2 = img.getpixel((x2, y1))
        p3 = img.getpixel((x1, y2))
        p4 = img.getpixel((x2, y2))

        pixels = [p1, p2, p3, p4]

        brightness = [
            0.299*r + 0.587*g + 0.114*b
            for r, g, b in pixels
        ]

        Imax = max(brightness)
        Imin = min(brightness)

        I = int((Imax + Imin) / 2)

        result.putpixel((x, y), (I, I, I))

result.save("potworek_d.png")
result.show()