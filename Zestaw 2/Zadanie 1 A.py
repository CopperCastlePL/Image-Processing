import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Zad1Values.csv")

r = df.iloc[:, 0]
I = df.iloc[:, 1]

# próbkowanie co 50 pikseli
step = 50
r_samples = r[::step]
I_samples = I[::step]

# wykres
plt.figure()
plt.plot(r, I, label="Sygnał ciągły")
plt.scatter(r_samples, I_samples, label="Próbki (co 50 px)")

plt.xlabel("r [piksele]")
plt.ylabel("I(r)")
plt.legend()
plt.title("Próbkowanie sygnału")

plt.show()