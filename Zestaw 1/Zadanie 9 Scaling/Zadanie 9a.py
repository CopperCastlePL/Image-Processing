from PIL import Image

img = Image.open("potworek_pixelart.png")

width, height = img.size

new_width = width * 10
new_height = height * 10

scaled = img.resize((new_width, new_height), Image.NEAREST)

scaled.save("potworek_a.png")

scaled.show()