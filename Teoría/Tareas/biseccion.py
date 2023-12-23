# considera f(x) = sen(x) aproxime el valor de pi usando bisección

import math

def funcion(x):
    return math.sin(x)  # f(x) = sen(x) 

def biseccion(f, a, b, tolerancia=1e-6, max_iteraciones=100):
    if f(a) * f(b) >= 0:
        raise ValueError("No existe una raíz en el intervalo dado")
    i = 0
    while (b - a) / 2 > tolerancia and i < max_iteraciones:
        c = (a + b) / 2 # se suman y se obtiene el punto medio
        if f(c) == 0: 
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        i = i+ 1
    raiz = (a + b) / 2 # se realiza nuevamente lo mismo
    return raiz

raiz = biseccion(funcion, 2, 4, tolerancia=1e-6, max_iteraciones=100) # se llama nuevamente a la funcion
if raiz is not None:
    aprox = raiz
    print("La aproximación usando método de bisección es:", aprox)
else:
    print("No se encontró una raíz")
