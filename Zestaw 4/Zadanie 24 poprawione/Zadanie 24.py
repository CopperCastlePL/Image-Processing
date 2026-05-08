import numpy as np
from scipy.signal import convolve2d
from PIL import Image
import matplotlib.pyplot as plt

# --- 1. Wczytanie obrazu ---
img = Image.open("Lego_GwiazdaSmierci_filtered.png").convert("L")
g = np.array(img, dtype=float) / 255.0  # normalizacja

# --- 2. Definicja filtru (5x5 dwumian Newtona) ---
h = np.array([
    [1, 4, 6, 4, 1],
    [4,16,24,16,4],
    [6,24,36,24,6],
    [4,16,24,16,4],
    [1, 4, 6, 4, 1]
], dtype=float) / 256.0

# --- 3. Funkcja Van‑Citterta ---
def van_cittert(g, h, iterations):
    f = g.copy()
    for i in range(iterations):
        conv = convolve2d(f, h, mode="same", boundary="symm")
        f = f + (g - conv)
    return f

# --- 4. Iteracje ---
iterations_list = [2, 5, 15]
results = {k: van_cittert(g, h, k) for k in iterations_list}

# --- 5. Symetryczna różnica ---
differences = {k: np.abs(g - results[k]) for k in iterations_list}

# --- 6. Wizualizacja ---
fig, axs = plt.subplots(3, 3, figsize=(12, 8))
axs[0, 0].imshow(g, cmap="gray")
axs[0, 0].set_title("Wejściowy")
axs[0, 0].axis("off")

for i, k in enumerate(iterations_list):
    axs[i, 1].imshow(results[k], cmap="gray")
    axs[i, 1].set_title(f"k = {k}")
    axs[i, 1].axis("off")

    axs[i, 2].imshow(differences[k], cmap="gray")
    axs[i, 2].set_title(f"Różnica k={k}")
    axs[i, 2].axis("off")

plt.tight_layout()
plt.show()

# --- 7. Zapis wyników ---
for k in iterations_list:
    Image.fromarray((results[k] * 255).clip(0, 255).astype(np.uint8)).save(f"result_k{k}.png")
    Image.fromarray((differences[k] * 255).clip(0, 255).astype(np.uint8)).save(f"difference_k{k}.png")
