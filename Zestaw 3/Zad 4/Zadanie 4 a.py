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


T = otsu_threshold(img_np)
print("Próg Otsu:", T)

binary = (img_np > T).astype(np.uint8) * 255

plt.imshow(binary, cmap='gray')
plt.title("Otsu global")
plt.axis('off')
plt.show()

Image.fromarray(binary).save("a_otsu.png")