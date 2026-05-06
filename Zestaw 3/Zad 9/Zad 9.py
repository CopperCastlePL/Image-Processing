from PIL import Image
import numpy as np

# =========================
# Wczytanie obrazu (np. z b lub c)
# =========================
img = Image.open("RezydencjaDiabla_equal.png").convert("L")
img_np = np.array(img)

# =========================
# LUT - 3 funkcje z diagramu
# =========================

def clip(x):
    return np.clip(x, 0, 255)

L = 256

R = np.zeros(L)
G = np.zeros(L)
B = np.zeros(L)

# -------------------------
# BLUE
# -------------------------
for x in range(L):
    if x < 31:
        B[x] = 128 + (255 - 128) * (x / 31)
    elif x < 95:
        B[x] = 255
    elif x < 159:
        B[x] = 255 * (1 - (x - 95) / (159 - 95))
    else:
        B[x] = 0

# -------------------------
# RED
# -------------------------
for x in range(L):
    if x < 31:
        R[x] = 0
    elif x < 95:
        R[x] = 255 * ((x - 31) / (95 - 31))
    elif x < 159:
        R[x] = 255
    elif x < 223:
        R[x] = 255 * (1 - (x - 159) / (223 - 159))
    else:
        R[x] = 0

# -------------------------
# GREEN
# -------------------------
for x in range(L):
    if x < 95:
        G[x] = 0
    elif x < 159:
        G[x] = 255 * ((x - 95) / (159 - 95))
    elif x < 223:
        G[x] = 255
    else:
        G[x] = 255 - (255 - 128) * ((x - 223) / (255 - 223))

# =========================
# Złożenie obrazu RGB
# =========================
R = R.astype(np.uint8)
G = G.astype(np.uint8)
B = B.astype(np.uint8)

out_r = R[img_np]
out_g = G[img_np]
out_b = B[img_np]

out_img = np.stack([out_r, out_g, out_b], axis=2)

# =========================
# Zapis wyniku
# =========================
result = Image.fromarray(out_img)
result.save("color_contrast.png")
result.show()