from PIL import Image
import numpy as np

# 1. Wczytanie obrazów
orig = Image.open("ptaki.png").convert("L")
orig_np = np.array(orig, dtype=np.float64)

b_img = Image.open("ptaki_sinus_smooth.png").convert("L")
b_np = np.array(b_img, dtype=np.float64)

# 2. Średnia jasność oryginału
target_mean = orig_np.mean()

# 3. Funkcja korekcji gamma
def apply_gamma(img, gamma):
    img_norm = img / 255.0
    corrected = np.power(img_norm, gamma) * 255.0
    return corrected

# 4. Binary search gamma (0.1–5.0)
low, high = 0.1, 5.0
for _ in range(30):  # wystarczająco dokładne
    mid = (low + high) / 2
    test = apply_gamma(b_np, mid)
    if test.mean() > target_mean:
        high = mid
    else:
        low = mid

gamma = (low + high) / 2
print("Dobrane gamma =", gamma)

# 5. Zastosowanie gamma
result = apply_gamma(b_np, gamma)
result = np.clip(result, 0, 255).astype(np.uint8)

Image.fromarray(result).save("ptaki_gamma.png")
