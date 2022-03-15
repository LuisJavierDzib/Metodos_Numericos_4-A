import numpy as np
from matplotlib import pyplot as plt

def funcion(x):
    return np.tan(x)-3.5

def funcion2(x):
    return np.power((1/np.cos(x)), 2)
w = np.pi

def newton(xi, maxiteraciones, cota):
    error = 1
    i = 1
    while error > cota:
        xr = xi - (funcion(xi)/funcion2(xi))
        error = np.abs((xr-xi)/xr)
        xi = xr
        i += 1
        print("Raiz:", xr, " Error:", error)

newton(0, w, 0.05)

vectorx = np.arange(1, 1.5, 0.01)

plt.plot(vectorx, funcion(vectorx))
plt.grid("x")
plt.grid("y")
plt.show()