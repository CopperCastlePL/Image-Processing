import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

f = np.array([
    [255,255,255,255,255,255,255],
    [255,255,255,255,255,255,255],
    [255,255,0,  0,  0,  255,255],
    [255,255,0,  0,  0,  255,255],
    [255,255,0,  0,  0,  255,255],
    [255,255,255,255,255,255,255],
    [255,255,255,255,255,255,255]
], dtype=float)

h1 = np.array([[1],[-1],[0]])
h2 = np.array([[0],[1],[-1]])

conv1 = convolve2d(f, h1, mode='same', boundary='symm', fillvalue=0)
conv2 = convolve2d(f, h2, mode='same', boundary='symm', fillvalue=0)

fig, axs = plt.subplots(1, 3, figsize=(10,4))
axs[0].imshow(f, cmap='gray')
axs[0].set_title('Oryginał f')
axs[1].imshow(conv1, cmap='gray')
axs[1].set_title('f * h1')
axs[2].imshow(conv2, cmap='gray')
axs[2].set_title('f * h2')
plt.show()
