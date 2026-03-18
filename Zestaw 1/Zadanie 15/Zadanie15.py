import numpy as np
from PIL import Image

img = Image.open("lwy.png").convert("L")
I = np.array(img, dtype=np.float32)

h, w = I.shape

# Bayer 4x4
B = np.array([
    [0, 8, 2, 10],
    [12, 4, 14, 6],
    [3, 11, 1, 9],
    [15, 7, 13, 5]
], dtype=np.float32)

# Znormalizowana macierz progów (0..1)
M = (B + 0.5) / 16.0

# Poziomy szarości
levels = np.array([0, 64, 128, 192, 255], dtype=np.float32)
N = len(levels)

out = np.zeros_like(I)

for y in range(h):
    for x in range(w):
        g = I[y, x] / 255.0 # v
        k_real = g * (N - 1) # 0..4
        k = int(np.floor(k_real))    # poziom bazowy
        f = k_real - k # część ułamkowa

        ty = y % 4
        tx = x % 4
        t = M[ty, tx]  # próg z Bayera

        if f > t and k < N - 1:
            k += 1

        out[y, x] = levels[k]

out_img = Image.fromarray(out.astype(np.uint8))
out_img.save("wyjscie_dither_5lvl.png")
