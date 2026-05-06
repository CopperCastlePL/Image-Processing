from PIL import Image
import numpy as np

# 1. Wczytanie obrazu (nie jest konieczne do samego Hhyper, ale zwykle wymagane w zadaniu)
img = Image.open("RezydencjaDiabla.png").convert("L")
img_np = np.array(img)

# 2. Parametry
L = 256
alpha = -1/3

# 3. Funkcja hiperbolizacji
def H_hyper(g, alpha=alpha, L=L):
    return ( (L - 1) * g ) / ( g + alpha * (L - 1 - g) )

# 4. LUT (mapa transformacji dla całego zakresu 0–255)
hyper_map = np.zeros(256, dtype=np.float64)

for g in range(256):
    hyper_map[g] = H_hyper(g)

# zaokrąglenie i ograniczenie do [0,255]
hyper_map = np.clip(np.round(hyper_map), 0, 255).astype(np.uint8)

# 5. (opcjonalnie) obraz po transformacji
img_hyper = hyper_map[img_np]
Image.fromarray(img_hyper).save("RezydencjaDiabla_hyper.png")

# 6. Wartości dla zadanych g
for g in [40, 45, 50]:
    print(f"Hhyper({g}) = {hyper_map[g]}")