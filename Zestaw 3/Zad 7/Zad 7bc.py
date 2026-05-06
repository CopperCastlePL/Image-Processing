from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# =========================
# Wczytanie obrazu
# =========================
img = Image.open("RezydencjaDiabla.png").convert("L")
img_np = np.array(img)

L = 256
N = img_np.size

# =========================
# (b) WYRÓWNANIE HISTOGRAMU
# =========================

hist = np.bincount(img_np.flatten(), minlength=256)
cdf = hist.cumsum()

cdf_min = cdf[cdf > 0].min()

cdf_norm = (cdf - cdf_min) / (N - cdf_min)
equal_map = np.floor(cdf_norm * 255).astype(np.uint8)

img_equal = equal_map[img_np]

# zapis obrazu
Image.fromarray(img_equal).save("equalized.png")

# histogram obrazu po equalizacji
hist_equal = np.bincount(img_equal.flatten(), minlength=256)

plt.figure()
plt.bar(range(256), hist_equal, width=1)
plt.title("Histogram po wyrównaniu")
plt.xlabel("Intensywność")
plt.ylabel("Liczba pikseli")
plt.savefig("hist_equal.png")
plt.close()

# =========================
# (c) HIPERBOLIZACJA
# α = -1/3
# =========================

alpha = -1/3

def H_hyper(g):
    return (255 * g) / (g + alpha * (255 - g))

hyper_map = np.array([H_hyper(g) for g in range(256)])
hyper_map = np.clip(np.round(hyper_map), 0, 255).astype(np.uint8)

img_hyper = hyper_map[img_np]

# zapis obrazu
Image.fromarray(img_hyper).save("hyperbolic.png")

# histogram obrazu po hiperbolizacji
hist_hyper = np.bincount(img_hyper.flatten(), minlength=256)

plt.figure()
plt.bar(range(256), hist_hyper, width=1)
plt.title("Histogram po hiperbolizacji (α = -1/3)")
plt.xlabel("Intensywność")
plt.ylabel("Liczba pikseli")
plt.savefig("hist_hyper.png")
plt.close()

# =========================
# Wartości wymagane w zadaniu
# =========================

for g in [40, 45, 50]:
    print("b) H_equal({}) = {}".format(g, equal_map[g]))
    print("c) H_hyper({}) = {}".format(g, hyper_map[g]))