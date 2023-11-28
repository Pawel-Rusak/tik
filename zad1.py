# Technologie informacyjne i komunikacyjne
# Python - zadania.
# Zadanie 1. plots – Rysowanie wykresów funkcji.

import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    return 1/3 * np.sin(3*x)

def f2(x):
    return 1/5 * np.sin(5*x)

def f3(x):
    return 1/9 * np.sin(9*x)




x = np.linspace(-8, 8, 500)


fig, ax = plt.subplots()

ax.set_xlim(-1.3 , 1.3)
ax.set_ylim(-0.4, 0.4)

ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Paweł Rusak Rysowanie wykresów funkcji.")

ax.plot(x, f1(x), "-y", label = r"$y = \frac{1}{3}  \sin(3x)$")
ax.plot(x, f2(x), "--r", label = r"$y = \frac{1}{5}  \sin(5x)$")
ax.plot(x, f3(x), ":b", label = r"$y = \frac{1}{9}  \sin(9x)$")

ax.legend()

plt.show()


ax.grid()
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_title("Paweł Rusak Zadanie 1. Rysowanie wykresów funkcji.")

ax.plot(x, f1(x), "-y", label = r"$y = \frac{1}{3}  \sin(3x)$")
ax.plot(x, f2(x), "--r", label = r"$y = \frac{1}{5}  \sin(5x)$")
ax.plot(x, f3(x), ":b", label = r"$y = \frac{1}{9}  \sin(9x)$")

fig.savefig("zad1.pdf")
