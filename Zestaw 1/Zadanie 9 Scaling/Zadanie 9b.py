from PIL import Image

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

        x1 = int(src_x)
        x2 = min(x1 + 1, width - 1)

        y1 = int(src_y)

        # pobranie dwóch pikseli
        p1 = img.getpixel((x1, y1))
        p2 = img.getpixel((x2, y1))

        r = (p1[0] + p2[0]) // 2
        g = (p1[1] + p2[1]) // 2
        b = (p1[2] + p2[2]) // 2

        result.putpixel((x, y), (r, g, b))

result.save("potworek_b.png")
result.show()