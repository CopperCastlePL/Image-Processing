from PIL import Image
import numpy as np

img = Image.open("bakterieRGB.png").convert("RGB")
edges = Image.open("bakterie_krawedzie.png").convert("L").resize(img.size)

img_np = np.array(img)
edges_np = np.array(edges)

# maska binarna
M = edges_np > 0

# pełny cyjan na krawędziach
img_np[M] = [0, 255, 255]

Image.fromarray(img_np).save("bakterie_cyjan_mocne.png")
