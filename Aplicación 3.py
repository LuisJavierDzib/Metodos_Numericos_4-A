from scipy.optimize import fsolve
import numpy as np
from matplotlib import pyplot as plt


def f(i):
    A = 750000
    P = 1500
    n = 20 * 12
    return (A - (P / i) * ((1 + i) ** n - 1))


int_mensual = fsolve(f, 0.1)

print("la tasa de interés anual es:" + str(int_mensual * 12 * 100))


vectorx = np.arange(0, 10, 0.01)

plt.plot(vectorx, f(vectorx))
plt.grid("x")
plt.grid("y")
plt.show()