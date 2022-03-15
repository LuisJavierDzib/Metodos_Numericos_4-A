import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.power(x, 4)-3*np.power(x, 2)-3

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
        if(error <= 0.01):
            print("Raiz: ", xr, " f(raíz): ", f(xr))
            print("error: ", error)

secante(1, 2, 0.01, 10)

x = np.linspace(1, 2, 7)
plt.plot(x, f(x))
plt.grid()
plt.show()
