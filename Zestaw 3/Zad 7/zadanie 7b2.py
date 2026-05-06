from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 1. Wczytanie obrazu w skali szarości
img = Image.open("RezydencjaDiabla.png").convert("L")
img_np = np.array(img)

# 2. Histogram
hist = np.bincount(img_np.flatten(), minlength=256)

# 3. CDF (skumulowany histogram)
cdf = hist.cumsum()

# 4. Normalizacja CDF
cdf_min = cdf[cdf > 0].min()
N = hist.sum()
cdf_norm = (cdf - cdf_min) / (N - cdf_min)

# 5. LUT (mapa transformacji)
L = 255
equalization_map = np.floor(cdf_norm * L).astype(np.uint8)

# 6. Obraz po wyrównaniu histogramu
img_equal = equalization_map[img_np]

# 7. Zapis obrazu
Image.fromarray(img_equal).save("RezydencjaDiabla_equal.png")

# 8. Histogram obrazu po equalizacji
hist_equal = np.bincount(img_equal.flatten(), minlength=256)

plt.figure(figsize=(10,4))
plt.bar(range(256), hist_equal, width=1.0, color='black')
plt.title("Histogram po wyrównaniu")
plt.xlabel("Poziom jasności")
plt.ylabel("Liczność")
plt.show()

# 9. Funkcja Hequal(g)
def H_equal(g):
    return equalization_map[g]

# 10. Wyniki dla g = 40, 45, 50
for g in [40, 45, 50]:
    print(f"H_equal({g}) = {H_equal(g)}")
