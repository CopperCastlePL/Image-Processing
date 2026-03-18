import numpy as np
from PIL import Image

img = Image.open("lwy.png").convert("L")
I = np.array(img, dtype=np.float32)

h, w = I.shape

dithering_matrix = np.array([
    [7, 1, 5],
    [3, 0, 2],
    [4, 8, 6]
], dtype=np.float32)

T = (dithering_matrix + 0.5) / 9 * 255

levels = np.linspace(0, 255, 9)

out = np.zeros_like(I)

# Dithering
for y in range(h):
    for x in range(w):
        pixel = I[y, x]

        # wybór progu z macierzy 3x3 (powtarzanie kafelkowe)
        ty = y % 3
        tx = x % 3
        threshold = T[ty, tx]

        # porównanie i kwantyzacja
        idx = np.searchsorted(levels, pixel + threshold - 128) - 1
        idx = np.clip(idx, 0, len(levels) - 1)

        out[y, x] = levels[idx]

out_img = Image.fromarray(out.astype(np.uint8))
out_img.save("lwy variable threshold.png")

print("Gotowe!")
