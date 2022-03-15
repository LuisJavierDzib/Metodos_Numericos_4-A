import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*np.sin(np.pi*x)+x

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
            print("Raiz: " , xr)

secante(1.5, 2, 0.01, 10)

x = np.linspace(1, 2, 7)
plt.plot(x, f(x))
plt.grid()
plt.show()
