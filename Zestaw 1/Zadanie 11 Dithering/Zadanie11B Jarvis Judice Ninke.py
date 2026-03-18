import numpy as np
from PIL import Image

img = Image.open("lwy.png").convert("L")
img = np.array(img, dtype=float)

h, w = img.shape

def quantize(v):
    if v < 32:
        return 0
    elif v < 96:
        return 64
    elif v < 160:
        return 128
    elif v < 224:
        return 192
    else:
        return 255

for y in range(h):
    for x in range(w):

        old = img[y,x]
        new = quantize(old)
        img[y,x] = new

        err = old - new

        diffusion = [
            (1,0,7),(2,0,5),
            (-2,1,3),(-1,1,5),(0,1,7),(1,1,5),(2,1,3),
            (-2,2,1),(-1,2,3),(0,2,5),(1,2,3),(2,2,1)
        ]

        for dx,dy,wg in diffusion:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < w and 0 <= ny < h:
                img[ny,nx] += err * wg / 48

result = Image.fromarray(np.clip(img,0,255).astype(np.uint8))
result.save("lwy_JJN_5.png")