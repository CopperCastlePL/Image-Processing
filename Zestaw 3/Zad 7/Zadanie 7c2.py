from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 1. Wczytanie obrazu
img = Image.open("RezydencjaDiabla.png").convert("L")
img_np = np.array(img)

# 2. Parametry
L = 256
alpha = -1/3

# 3. Funkcja hiperbolizacji
def H_hyper(g, alpha=alpha, L=L):
    return ( (L - 1) * g ) / ( g + alpha * (L - 1 - g) )

# 4. LUT
hyper_map = np.zeros(256, dtype=np.float64)
for g in range(256):
    hyper_map[g] = H_hyper(g)

hyper_map = np.clip(np.round(hyper_map), 0, 255).astype(np.uint8)

# 5. Obraz po hiperbolizacji
img_hyper = hyper_map[img_np]
Image.fromarray(img_hyper).save("RezydencjaDiabla_hyper.png")

# 6. Histogram obrazu po hiperbolizacji
hist_hyper = np.bincount(img_hyper.flatten(), minlength=256)

plt.figure(figsize=(10,4))
plt.bar(range(256), hist_hyper, width=1.0, color='black')
plt.title("Histogram po hiperbolizacji")
plt.xlabel("Poziom jasności")
plt.ylabel("Liczność")
plt.show()

# 7. Wartości Hhyper(g)
for g in [40, 45, 50]:
    print(f"Hhyper({g}) = {hyper_map[g]}")
