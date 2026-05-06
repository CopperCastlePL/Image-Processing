from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# wczytanie obrazu w skali szarości
img = Image.open("RezydencjaDiabla.png").convert("L")

# histogram (Pillow zwraca listę 256 wartości)
hist = img.histogram()

# konwersja do numpy i CDF (skumulowany histogram)
hist_np = np.array(hist)
cdf = hist_np.cumsum()

# normalizacja (opcjonalnie, żeby było 0–1)
cdf_norm = cdf / cdf[-1]

# wykres
plt.plot(cdf_norm)
plt.title("Skumulowany histogram (CDF)")
plt.xlabel("Poziom intensywności")
plt.ylabel("Skumulowana częstość")
plt.grid(True)
plt.show()