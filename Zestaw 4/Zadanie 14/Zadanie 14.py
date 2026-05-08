from PIL import Image
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

# --- 1. Wczytanie obrazu g ---
g = Image.open("Odd_Moon.png").convert("L")
g = np.array(g, dtype=float)

# --- 2. Definicja filtrów ---
# h1 – filtr uśredniający 3×3
h1 = np.ones((3, 3), dtype=float) / 9.0

# h2 – filtr gradientowy poziomy 1×3
h2 = np.array([[0, 1, -1]], dtype=float)

# --- 3. Sploty ---
# g1 = g * h1
g1 = convolve2d(g, h1, mode="same", boundary="symm")

# g2 = g1 * h2
g2 = convolve2d(g1, h2, mode="same", boundary="symm")

# --- 4. Wizualizacja ---
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

axs[0].imshow(g, cmap="gray")
axs[0].set_title("Oryginał g")

axs[1].imshow(g1, cmap="gray")
axs[1].set_title("g1 = g * h1")

axs[2].imshow(g2, cmap="gray")
axs[2].set_title("g2 = g1 * h2")

plt.tight_layout()
plt.show()
