from PIL import Image, ImageDraw
import random

img = Image.open("img.png").convert("RGB")
width, height = img.size

result = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(result)

liczba_kropek = 200000
promien = 3

for _ in range(liczba_kropek):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)

    kolor = img.getpixel((x, y))

    draw.ellipse((x - promien, y - promien, x + promien, y + promien), fill=kolor, outline=None)

result.save("pointylizm.png")
result.show()