import cv2
import numpy as np
import matplotlib.pyplot as plt

# ---- 1. Wczytanie obrazu ----
img = cv2.imread("Lego_GwiazdaSmierci_filtered.png", cv2.IMREAD_GRAYSCALE)
img = img.astype(np.float32) / 255.0

# ---- 2. Definicja filtra (5x5 dwumian Newtona) ----
kernel = np.array([
    [1, 4, 6, 4, 1],
    [4,16,24,16,4],
    [6,24,36,24,6],
    [4,16,24,16,4],
    [1, 4, 6, 4, 1]
], dtype=np.float32)

kernel = kernel / 256.0

# ---- 3. Funkcja Van-Citterta ----
def van_cittert(g, h, iterations):
    f = g.copy()  # start: obraz wejściowy

    for i in range(iterations):
        conv = cv2.filter2D(f, -1, h)
        f = f + (g - conv)

    return f

# ---- 4. Iteracje ----
iterations_list = [2, 5, 15]
results = {}

for k in iterations_list:
    results[k] = van_cittert(img, kernel, k)

# ---- 5. Symetryczna różnica ----
def symmetric_difference(a, b):
    return np.abs(a - b)

differences = {}
for k in iterations_list:
    differences[k] = symmetric_difference(img, results[k])

# ---- 6. Wyświetlanie ----
plt.figure(figsize=(12,8))

plt.subplot(3,3,1)
plt.title("Wejściowy")
plt.imshow(img, cmap='gray')
plt.axis('off')

for i, k in enumerate(iterations_list):
    plt.subplot(3,3,i+2)
    plt.title(f"k = {k}")
    plt.imshow(results[k], cmap='gray')
    plt.axis('off')

    plt.subplot(3,3,i+5)
    plt.title(f"Różnica k={k}")
    plt.imshow(differences[k], cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.show()

# ---- 7. Zapis do plików ----
for k in iterations_list:
    cv2.imwrite(f"result_k{k}.png", (results[k]*255).clip(0,255).astype(np.uint8))
    cv2.imwrite(f"difference_k{k}.png", (differences[k]*255).clip(0,255).astype(np.uint8))