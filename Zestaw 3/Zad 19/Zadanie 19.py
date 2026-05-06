from PIL import Image
import numpy as np

# Wczytanie obrazu
img = Image.open("HelicobacterPylori_modified.png").convert("L")
img_np = np.array(img)

# Ekstrakcja płaszczyzn bitowych
bit_planes = []

for i in range(8):
    plane = (img_np >> i) & 1  # wyciągnięcie i-tego bitu
    plane = (plane * 255).astype(np.uint8)  # wizualizacja (0/255)

    Image.fromarray(plane).save(f"bit_plane_{i}.png")
    bit_planes.append(plane)

print("Zapisano wszystkie płaszczyzny bitowe.")