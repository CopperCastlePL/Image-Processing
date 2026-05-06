from PIL import Image
import numpy as np

# Wczytanie obrazu po filtracji (b)
img_b = Image.open("ptaki_sinus_smooth.png").convert("L")
img_b_np = np.array(img_b, dtype=np.float64)

# Wczytanie obrazu referencyjnego
img_ref = Image.open("ptaki.png").convert("L")
img_ref_np = np.array(img_ref, dtype=np.float64)

# Średnia jasność
mean_b = np.mean(img_b_np)
mean_ref = np.mean(img_ref_np)

print("Mean (b):", mean_b)
print("Mean (ref):", mean_ref)


# Funkcja gamma
def apply_gamma(image, gamma):
    normalized = image / 255.0
    corrected = np.power(normalized, gamma)
    return np.clip(corrected * 255, 0, 255)


# Szukanie najlepszego gamma
best_gamma = None
best_diff = float("inf")

for gamma in np.linspace(0.1, 3.0, 100):
    corrected = apply_gamma(img_b_np, gamma)
    mean_corr = np.mean(corrected)
    diff = abs(mean_corr - mean_ref)

    if diff < best_diff:
        best_diff = diff
        best_gamma = gamma

print("Best gamma:", best_gamma)

# Zastosowanie najlepszego gamma
final_img = apply_gamma(img_b_np, best_gamma)
final_img = final_img.astype(np.uint8)

# Zapis
Image.fromarray(final_img).save("ptaki_gamma.png")