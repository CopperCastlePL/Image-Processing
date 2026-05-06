import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

def to_gray(img):
    """Konwersja RGB → grayscale"""
    if img.ndim == 3:
        return img.mean(axis=2)
    return img

def normalize_to_uint8(img):
    """Normalizacja do zakresu 0–255"""
    img = np.clip(img, 0, 255)
    return img.astype(np.uint8)

# ---------------------------------------------------------
# 1. Wczytanie obrazu (Pillow)
# ---------------------------------------------------------
img = Image.open("nosorozec.png")
f = np.array(img).astype(np.float64)

f_gray = to_gray(f)

# ---------------------------------------------------------
# 2. Filtr Gaussa
# ---------------------------------------------------------
sigma = 2
g = gaussian_filter(f_gray, sigma=sigma)

Image.fromarray(normalize_to_uint8(g)).save("nosorozec_gauss.png")

# ---------------------------------------------------------
# 3. Unsharp mask
# ---------------------------------------------------------
mask = f_gray - g

# normalizacja do wizualizacji
mask_norm = mask - mask.min()
mask_norm = mask_norm / mask_norm.max() * 255

Image.fromarray(normalize_to_uint8(mask_norm)).save("nosorozec_unsharp_mask.png")

# ---------------------------------------------------------
# 4. Highboost filtering
# ---------------------------------------------------------
A = 0.5
f_hb = f_gray + A * mask

Image.fromarray(normalize_to_uint8(f_hb)).save("nosorozec_highboost.png")

print("Gotowe!")