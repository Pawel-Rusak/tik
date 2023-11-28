# Technologie informacyjne i komunikacyjne
# Przykłady - analiza danych doświadczalnych.
# Przykład 1. Dopasowanie prostej do danych doświadczalnych.

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize


###############################################################################
# Wczytanie danych doświadczalnych.
###############################################################################

data = np.loadtxt("zad2.txt")
v = data[:, 0] # [wiersz, kolumna], tu: wszystkie wiersze i pierwsza (zerowa) kolumna.
a = data[:, 1] # [wiersz, kolumna], tu: wszystkie wiersze i druga (pierwsza) kolumna.



###############################################################################
# Dopasowanie prostej y = a x + b do danych doświadczalnych.
###############################################################################

# Funkcja zadająca krzywą y = f(x), która ma zostać dopasowana.
# Na liście argumentów muszą się też znaleźć parametry dopasowania: a i b.
def f(v, A, B):
    return 9.8 - A/0.5 * v**B

# Krotka zawierająca początkowe wartości parametrów dopasowania: a i b.
p0 = (0, 0)

# scipy.optimize.curve_fit dokonuje dopasowania.
# p będzie tablicą (ndarray) zawierającą dopasowane parametry.
# pcov będzie tablicą (ndarray) zawierającą macierz kowariancji.
p, pcov = scipy.optimize.curve_fit(f, v, a, p0)


###############################################################################
# Prezentacja danych doświadczalnych i wyników dopasowania.
###############################################################################

# Wypisujemy wyniki na standardowe wyjście.
print("Dopasowanie krzywej a = g - A/m * v^B")
print(f"   Parametry: {p}")
print(f"   Błędy: {np.sqrt(np.diag(pcov))}")

A=p[0]
B=p[1]
c=np.sqrt(np.diag(pcov))

# Wykreślamy dane doświadczalne wraz z dopasowaniem.
fig, ax = plt.subplots()

ax.grid()
ax.set_xlabel("Prędkość, $v$ [m/s]")
ax.set_ylabel("Przyspieszenie, $a$ [$\mathregular{m / s^2}$]")
ax.set_title("Paweł Rusak, A= "+str(A)+" B= "+str(B)+"\n Błędy: "+str(c))

ax.plot(v, a, "r+", label = "Dane doświadczalne")

# p jest tablicą, musimy napisać *p, aby przekazać jej wartości jako niezależne zmienne.
ax.plot(v, f(v, *p), "b", label = "Dopasowanie a = g - (A/m)$\mathregular{ v^{B}}$")

ax.legend()
plt.show()
fig.savefig("zad2.pdf")
