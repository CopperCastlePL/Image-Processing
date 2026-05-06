import cv2
import numpy as np
import matplotlib.pyplot as plt

# ---- 1. Wczytanie obrazu ----
img = cv2.imread("nosorozec.png", cv2.IMREAD_GRAYSCALE)
img = img.astype(np.float32) / 255.0

# ---- 2. Rozmycie Gaussa ----
blur = cv2.GaussianBlur(img, (5,5), sigmaX=1.0)

# ---- 3. Maska nieostrości ----
mask = img - blur

# ---- 4. Highboost filtering ----
k = 0.5
result = img + k * mask

# ---- 5. Normalizacja (żeby nie było poza zakresem)
result = np.clip(result, 0, 1)

# ---- 6. Wyświetlenie ----
plt.figure(figsize=(10,6))

plt.subplot(1,3,1)
plt.title("Oryginał")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,3,2)
plt.title("Maska nieostrości")
plt.imshow(mask, cmap='gray')
plt.axis('off')

plt.subplot(1,3,3)
plt.title("Highboost (k=0.5)")
plt.imshow(result, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

# ---- 7. Zapis ----
cv2.imwrite("unsharp_mask.png", ((mask - mask.min())/(mask.max()-mask.min())*255).astype(np.uint8))
cv2.imwrite("highboost_result.png", (result*255).astype(np.uint8))