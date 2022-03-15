import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.tan(np.pi*x)-6

def secante(xinf, xsup, cota, maxiteraciones):
    error = 1
    i = 1
    while error > cota:
        xr = xinf - ((f(xinf)*(xinf-xsup))/(f(xinf)-f(xsup)))
        error = np.abs((xr-xinf)/xr)
        print("Iteración:", i, " xsup:", xsup, "xinf:",
            xinf, " Raiz:", xr, " Error:", error)
        xinf = xsup
        xsup = xr
        i += 1
        if(error <= 0.001):
            print("Raiz: ", xr)

secante(0, 0.44, 0.001, 10)

vectorx = np.arange(.2, .5, 0.001)
plt.plot(vectorx, f(vectorx))
plt.grid("X")
plt.grid("Y")
plt.show()