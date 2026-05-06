from PIL import Image
import numpy as np

# 1. Wczytanie obrazu
img = Image.open("ptaki.png").convert("L")   # grayscale
img_np = np.array(img, dtype=np.float64)

# 2. Wymiary
H, W = img_np.shape

# 3. Okno sinusoidalne 2D
x = np.arange(W)
y = np.arange(H)

wx = np.sin(np.pi * x / (W - 1))
wy = np.sin(np.pi * y / (H - 1))

window = np.outer(wy, wx)   # tworzy okno 2D

# 4. Zastosowanie okna
img_windowed = img_np * window

# 5. Normalizacja do 0–255
img_windowed = np.clip(img_windowed, 0, 255).astype(np.uint8)

# 6. Zapis wyniku
Image.fromarray(img_windowed).save("ptaki_sinus.png")
