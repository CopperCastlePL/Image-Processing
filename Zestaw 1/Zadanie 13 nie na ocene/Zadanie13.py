import numpy as np

I = np.array([
    [160, 240],
    [55, 190]
], dtype=np.float32)

D = np.array([
    [6, 8, 4],
    [1, 0, 3],
    [5, 2, 7]
], dtype=np.float32)

# Poziomy kwantyzacji
levels = np.array([25, 50, 75, 100, 125, 150, 175, 200, 225])

# próg
T = (D + 0.5) / 9 * 255  # skala 0–255

out = np.zeros((6, 6), dtype=np.int32)

# Dithering
for y in range(2):
    for x in range(2):
        pixel = I[y, x]
        for dy in range(3):
            for dx in range(3):
                threshold = T[dy, dx]

                # wybór poziomu kwantyzacji
                idx = np.searchsorted(levels, pixel + threshold / 255 * 255) - 1
                idx = np.clip(idx, 0, len(levels) - 1)

                out[y * 3 + dy, x * 3 + dx] = levels[idx]

print("Obraz wyjściowy 6x6:")
print(out)
