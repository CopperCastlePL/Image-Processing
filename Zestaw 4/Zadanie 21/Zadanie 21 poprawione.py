from PIL import Image
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

# --- 1. Wczytanie obrazu ---
g = Image.open("Escher.png").convert("L")
g = np.array(g, dtype=float)

# --- 2. Definicja jądra Kirsha h1 ---
h1 = np.array([
    [-3, 5, 5],
    [-3, 0, 5],
    [-3, -3, -3]
], dtype=float)

# --- 3. Generacja pozostałych 7 jąder przez rotację co 45° ---
kernels = [np.rot90(h1, k) for k in range(8)]

# --- 4. Obliczenie odpowiedzi dla każdego kierunku ---
responses = [convolve2d(g, k, mode="same", boundary="symm") for k in kernels]

# --- 5. Maksimum z ośmiu kierunków ---
f = np.maximum.reduce(responses)

# --- 6. Normalizacja do zakresu 0–255 ---
f = (f - f.min()) / (f.max() - f.min()) * 255
f = f.astype(np.uint8)

# --- 7. Wizualizacja i zapis ---
Image.fromarray(f).save("Escher_Kirsch_SciPy.png")

plt.figure(figsize=(8, 6))
plt.imshow(f, cmap="gray")
plt.title("Krawędzie Kirsha (SciPy)")
plt.axis("off")
plt.show()
