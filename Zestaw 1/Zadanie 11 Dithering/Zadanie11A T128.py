import numpy as np
from PIL import Image

img = Image.open("lwy.png").convert("L")
img = np.array(img, dtype=float)

T = 128  # próg

h, w = img.shape

for y in range(h):
    for x in range(w):

        old_pixel = img[y, x]

        # progowanie
        new_pixel = 255 if old_pixel >= T else 0
        img[y, x] = new_pixel

        error = old_pixel - new_pixel

        # dyfuzja błędu Floyd–Steinberg
        if x+1 < w:
            img[y, x+1] += error * 7/16
        if y+1 < h and x > 0:
            img[y+1, x-1] += error * 3/16
        if y+1 < h:
            img[y+1, x] += error * 5/16
        if y+1 < h and x+1 < w:
            img[y+1, x+1] += error * 1/16


result = Image.fromarray(np.clip(img,0,255).astype(np.uint8))
result.save("lwy_dithering_T128.png")