import numpy as np
import matplotlib.pyplot as plt

L = 256
x = np.arange(L)

R = np.zeros(L)
G = np.zeros(L)
B = np.zeros(L)

# ---------------- RED ----------------
for i in range(L):
    if i < 31:
        R[i] = 0
    elif i < 95:
        R[i] = 255 * (i - 31) / (95 - 31)
    elif i < 159:
        R[i] = 255
    elif i < 223:
        R[i] = 255 * (1 - (i - 159) / (223 - 159))
    else:
        R[i] = 0

# ---------------- GREEN ----------------
for i in range(L):
    if i < 95:
        G[i] = 0
    elif i < 159:
        G[i] = 255 * (i - 95) / (159 - 95)
    elif i < 223:
        G[i] = 255
    else:
        G[i] = 255 - (255 - 128) * (i - 223) / (255 - 223)

# ---------------- BLUE ----------------
for i in range(L):
    if i < 31:
        B[i] = 128 + (255 - 128) * (i / 31)
    elif i < 95:
        B[i] = 255
    elif i < 159:
        B[i] = 255 * (1 - (i - 95) / (159 - 95))
    else:
        B[i] = 0

# ---------------- PLOT ----------------
plt.plot(x, R, 'r', label='Red')
plt.plot(x, G, 'g', label='Green')
plt.plot(x, B, 'b', label='Blue')

plt.title("Diagram")
plt.xlabel("Wejściowa skala szarości")
plt.ylabel("Wyjściowa intensywność")
plt.legend()
plt.grid(True)
plt.show()