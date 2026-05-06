from PIL import Image
import numpy as np

# Wczytanie obrazu w skali szarości
g = Image.open("Escher.png").convert("L")
g = np.array(g, dtype=np.uint8)

# Definicja jądra Kirsha h1
h1 = np.array([[-3, 5, 5],
               [-3, 0, 5],
               [-3, -3, -3]], dtype=np.int8)

# Generacja pozostałych 7 jąder przez rotację co 45°
kernels = [np.rot90(h1, k) for k in range(8)]

# Funkcja splotu 3x3 dla obrazu 8-bitowego
def convolve(img, kernel):
    h, w = img.shape
    out = np.zeros_like(img, dtype=np.int16)
    for i in range(1, h-1):
        for j in range(1, w-1):
            region = img[i-1:i+2, j-1:j+2]
            out[i, j] = np.sum(region * kernel)
    return out

# Obliczenie odpowiedzi dla każdego kierunku
responses = [convolve(g, k) for k in kernels]

# Maksimum z ośmiu kierunków
f = np.maximum.reduce(responses)

# Normalizacja do 0–255 (8-bit)
f = np.clip(f, 0, 255).astype(np.uint8)

# Zapis i podgląd
Image.fromarray(f).save("Escher_kirsch.png")
Image.fromarray(f).show()
