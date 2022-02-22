import math

x = -5
e_to_2 = 0
for i in range(30):
    e_to_2 += x**i/math.factorial(i)

print(e_to_2)

#Resultado con redondeo
round(e_to_2,3)
