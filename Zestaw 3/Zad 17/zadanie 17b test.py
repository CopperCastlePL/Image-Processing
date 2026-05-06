from PIL import Image
import numpy as np

# 1. Wczytanie obrazu z (a)
img = Image.open("ptaki_sinus.png").convert("L")
img_np = np.array(img, dtype=np.float64)

# 2. Przygotowanie pustej macierzy na wynik
H, W = img_np.shape
out = np.zeros_like(img_np)

# 3. Filtr uśredniający 3×3 (ręczna konwolucja)
for y in range(1, H-1):
    for x in range(1, W-1):
        region = img_np[y-1:y+2, x-1:x+2]   # okno 3×3
        out[y, x] = np.mean(region)

# 4. Normalizacja i zapis
out = np.clip(out, 0, 255).astype(np.uint8)
Image.fromarray(out).save("ptaki_sinus_smooth test.png")
