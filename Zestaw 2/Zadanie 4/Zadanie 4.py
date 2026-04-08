from PIL import Image
import numpy as np


def mse(imageA, imageB):
    # konwersja do numpy array
    arrA = np.array(imageA).astype("float")
    arrB = np.array(imageB).astype("float")

    # MSE
    err = np.mean((arrA - arrB) ** 2)
    return err


# wczytanie obrazów
ref = Image.open("osaRGB_PNG.png").convert("RGB")
gif = Image.open("osaRGB_GIF.gif").convert("RGB")
jpg = Image.open("osaRGB_JPG.jpg").convert("RGB")

# upewnij się, że mają ten sam rozmiar
gif = gif.resize(ref.size)
jpg = jpg.resize(ref.size)

# obliczenia
mse_gif = mse(ref, gif)
mse_jpg = mse(ref, jpg)

# Większe MSE większe zniekształcenia więc JPG lepszy bo mniejsze MSE
print("MSE (PNG vs GIF):", mse_gif)
print("MSE (PNG vs JPG):", mse_jpg)