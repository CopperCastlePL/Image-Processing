from PIL import Image
import numpy as np

# 1. Wczytanie obrazów
img = Image.open("bakterie.png").convert("RGB")
edges = Image.open("bakterie_krawedzie.png").convert("L").resize(img.size)

# 2. NumPy
img_np = np.array(img)
edges_np = np.array(edges)

# 3. Maska binarna krawędzi
M = edges_np > 0

# 4. Pełne nadpisanie kolorem czerwonym na krawędziach
img_np[M] = [255, 0, 0]

# 5. Zapis wyniku
Image.fromarray(img_np).save("bakterie_czerwone_mocne.png")
