from PIL import Image

img = Image.open("potworek_pixelart.png")

scaled = img.resize((500, 650), Image.BILINEAR)

scaled.save("potworek_c.png")
scaled.show()