from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# --- Wczytanie obrazu ---
img = Image.open("roze.png").convert("L")
img_np = np.array(img)


# --- pomocnicza funkcja: średnia w przedziale ---
def class_mean(hist, start, end):
    if end <= start:
        return 0

    indices = np.arange(start, end)
    total_pixels = hist[start:end].sum()

    if total_pixels == 0:
        return 0

    return np.sum(indices * hist[start:end]) / total_pixels


# --- ITERACYJNY OTSU 3 KLASY ---
def otsu_3class_iterative(image, delta=2):
    hist, _ = np.histogram(image.flatten(), bins=256, range=(0, 256))

    T1, T2 = 80, 170

    while True:
        mu0 = class_mean(hist, 0, int(T1))
        mu1 = class_mean(hist, int(T1), int(T2))
        mu2 = class_mean(hist, int(T2), 256)

        new_T1 = (mu0 + mu1) / 2
        new_T2 = (mu1 + mu2) / 2

        if abs(new_T1 - T1) < delta and abs(new_T2 - T2) < delta:
            T1, T2 = new_T1, new_T2
            break

        T1, T2 = new_T1, new_T2

    return T1, T2


# --- liczenie progów ---
T1, T2 = otsu_3class_iterative(img_np)
print("T1:", T1)
print("T2:", T2)


# --- progowanie 3-klasowe ---
segmented = np.zeros_like(img_np)

segmented[(img_np >= 0) & (img_np < T1)] = 0
segmented[(img_np >= T1) & (img_np < T2)] = 128
segmented[(img_np >= T2)] = 255


# --- wizualizacja (tylko wynik) ---
plt.figure(figsize=(6, 5))
plt.imshow(segmented, cmap='gray')
plt.title("Otsu 3-klasowy (iteracyjny)")
plt.axis('off')
plt.show()


# --- zapis wyniku ---
Image.fromarray(segmented.astype(np.uint8)).save("b_otsu.png")