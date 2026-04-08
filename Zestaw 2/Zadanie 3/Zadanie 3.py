from PIL import Image
import numpy as np


def load_grayscale(path):
    img = Image.open(path).convert("L")  # skala szarości
    return np.array(img)


def global_contrast(img):
    Imax = np.max(img)
    Imin = np.min(img)
    return (Imax - Imin) / (Imax + Imin + 1e-8)


def local_contrast(img):
    img = img.astype(float)
    h, w = img.shape
    contrasts = []

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            center = img[i, j]
            neighbors = img[i - 1:i + 2, j - 1:j + 2].flatten()
            neighbors = np.delete(neighbors, 4)  # usuwamy środek

            mean_n = np.mean(neighbors)
            c = abs(center - mean_n) / (center + mean_n + 1e-8)
            contrasts.append(c)

    return np.mean(contrasts)


files = ["tygrysA.png", "tygrysB.png", "tygrysC.png"]

for f in files:
    img = load_grayscale(f)

    print(f"{f}:")
    print(" Global contrast:", global_contrast(img))
    print(" Local contrast:", local_contrast(img))
    print()