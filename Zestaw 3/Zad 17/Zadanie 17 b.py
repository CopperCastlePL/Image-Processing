from PIL import Image
import numpy as np
from scipy.signal import convolve2d

# 1. Wczytanie obrazu z (a)
img = Image.open("ptaki_sinus.png").convert("L")
img_np = np.array(img, dtype=np.float64)

# 2. Maska filtru uśredniającego 3x3
kernel = np.ones((3, 3)) / 9.0

# 3. Konwolucja (z zachowaniem rozmiaru)
smoothed = convolve2d(img_np, kernel, mode='same', boundary='symm')

# 4. Normalizacja i zapis
smoothed = np.clip(smoothed, 0, 255).astype(np.uint8)
Image.fromarray(smoothed).save("ptaki_sinus_smooth.png")
