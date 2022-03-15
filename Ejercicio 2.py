import numpy as np
from matplotlib import pyplot as plt

def fx(t):
    return ((t*np.power(2.1-0.5*t, 2))/((1-t)*(np.power((1.1-0.5*t), 2))))-3.69

def biseccion(a, b, cota):
    error = 0.001
    i = 0
    listar = [1, 10]
    if fx(a)*fx(b) < 0:
        while error > cota:
            xr = (a+b)/2
            fxr = fx(xr)
            fxa = fx(a)
            if fxr * fxa < 0:
                b = xr
            elif fxr * fxa > 0:
                a = xr
            else:
                break
            listar.append(xr)
            xractual = xr
            if(len(listar) >= 2):
                xranterior = listar[-2]
                error = np.abs((xractual-xranterior)/xractual)
            else:
                error = 1
            i += 1
    else:
        print("No hay solucion")
    return listar

raices = biseccion(0, 1, 0.001)
print(raices)
print("X:", raices[-1])

vectorx = np.arange(0, 1, 0.1)
plt.plot(vectorx, fx(vectorx))
plt.grid("X")
plt.grid("Y")
plt.show()