from PIL import Image
import numpy as np

# Wczytanie obrazów
cover = Image.open("HelicobacterPylori_modified.png").convert("L")
secret = Image.open("secret.png").convert("L")

cover_np = np.array(cover)
secret_np = np.array(secret)

# Dopasowanie rozmiaru (ważne!)
secret = secret.resize(cover.size)
secret_np = np.array(secret)

# Zamiana obrazu ukrywanego na 0/1 (binarizacja)
secret_bin = (secret_np > 128).astype(np.uint8)

# Zerowanie najmłodszego bitu w obrazie bazowym
cover_cleared = cover_np & 0b11111110

# Wstawienie ukrytego obrazu do LSB
stego = cover_cleared | secret_bin

# Zapis
Image.fromarray(stego.astype(np.uint8)).save("stego.png")

print("Ukryty obraz zapisany jako stego.png")


extracted = (stego & 1) * 255
Image.fromarray(extracted.astype(np.uint8)).save("extracted.png")