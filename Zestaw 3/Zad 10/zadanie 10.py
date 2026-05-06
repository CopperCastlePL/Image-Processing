import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image_and_hist(img, title):
    plt.figure(figsize=(10,4))

    plt.subplot(1,2,1)
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.hist(img.ravel(), bins=256, range=(0,256))
    plt.title("Histogram")
    plt.show()

# 1. Wczytanie obrazu w skali szarości
img = cv2.imread("CalunTurynski.png", cv2.IMREAD_GRAYSCALE)
show_image_and_hist(img, "Oryginał")

# 2. Rozciąganie kontrastu (normalizacja)
img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
show_image_and_hist(img_norm, "Normalizacja kontrastu")

# 3. Equalizacja histogramu
img_eq = cv2.equalizeHist(img)
show_image_and_hist(img_eq, "Equalizacja histogramu")

# 4. CLAHE (lokalna equalizacja)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img_clahe = clahe.apply(img)
show_image_and_hist(img_clahe, "CLAHE")

# 5. Wzmocnienie (opcjonalnie gamma)
gamma = 1.5
img_gamma = np.power(img_clahe / 255.0, gamma) * 255
img_gamma = img_gamma.astype(np.uint8)
show_image_and_hist(img_gamma, "Gamma korekcja")