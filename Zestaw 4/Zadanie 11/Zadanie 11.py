from PIL import Image
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

# Wczytanie obrazu i konwersja do skali szarości
img = Image.open('skarpetyIPhone.png').convert('L')
img = np.array(img, dtype=float) / 255.0  # normalizacja do [0,1]

# Definicja filtrów (jak wcześniej)
h_a = np.array([
    [0, 0, 1, 0, 0],
    [0, 2, 2, 2, 0],
    [1, 2, 5, 2, 1],
    [0, 2, 2, 2, 0],
    [0, 0, 1, 0, 0]
], dtype=float)
h_a /= np.sum(h_a)

h_b = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]],
dtype=float)

h_c = np.array([
    [1, 0, -1],
    [1, 1, -1],
    [1, 0, -1]],
dtype=float)

h_d = np.array([
    [1, -1, -1],
    [1, -2, -1],
    [1, 1, 1]],
dtype=float)

filters = {'h_a': h_a, 'h_b': h_b, 'h_c': h_c, 'h_d': h_d}

# Filtracja
fig, axs = plt.subplots(1, 5, figsize=(15, 4))
axs[0].imshow(img, cmap='gray')
axs[0].set_title('Oryginał')

for i, (name, h) in enumerate(filters.items(), start=1):
    conv = convolve2d(img, h, mode='same', boundary='fill')
    axs[i].imshow(conv, cmap='gray')
    axs[i].set_title(name)

plt.tight_layout()
plt.show()
