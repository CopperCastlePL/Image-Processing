from PIL import Image
import numpy as np
from scipy.signal import convolve2d

# 1. Wczytanie oryginalnego obrazu
img = Image.open("ptaki.png").convert("L")
img_np = np.array(img, dtype=np.float64)

# 2. Filtr uśredniający 3x3
kernel = np.ones((3, 3)) / 9.0

# 3. Konwolucja
smoothed = convolve2d(img_np, kernel, mode='same', boundary='symm')

# 4. Zapis
smoothed = np.clip(smoothed, 0, 255).astype(np.uint8)
Image.fromarray(smoothed).save("ptaki_smooth.png")