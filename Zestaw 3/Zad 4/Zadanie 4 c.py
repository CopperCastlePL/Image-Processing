from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("roze.png").convert("L")  # grayscale
img_np = np.array(img)



def otsu_threshold(image):
    hist, _ = np.histogram(image.flatten(), bins=256, range=(0, 256))
    total = image.size

    sum_total = np.dot(np.arange(256), hist)

    sumB, wB, max_var, threshold = 0, 0, 0, 0

    for t in range(256):
        wB += hist[t]
        if wB == 0:
            continue

        wF = total - wB
        if wF == 0:
            break

        sumB += t * hist[t]

        mB = sumB / wB
        mF = (sum_total - sumB) / wF

        var_between = wB * wF * (mB - mF) ** 2

        if var_between > max_var:
            max_var = var_between
            threshold = t

    return threshold



def local_otsu(image, window_size=11):
    pad = window_size // 2
    padded = np.pad(image, pad, mode='reflect')

    output = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = padded[i:i + window_size, j:j + window_size]
            T = otsu_threshold(window)
            output[i, j] = 255 if image[i, j] > T else 0

    return output


local = local_otsu(img_np, 11)

plt.imshow(local, cmap='gray')
plt.title("Lokalne Otsu 11x11")
plt.axis('off')
plt.show()

Image.fromarray(local).save("c_otsu.png")