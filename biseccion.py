#!/usr/bin/python
#-*- coding:utf-8 -*-
from math import *

ecuacion = raw_input('Ingrese la función a resolver: ')
aValor = float(input('Ingrese el extremo izquierdo del intervalo: '))
bValor = float(input('Ingrese el extremo derecho del intervalo: '))
tolerancia = float(input('Ingrese la tolerancia del método: '))
maximoIteraciones = int(input('Ingrese el máximo de iteraciones a realizar: '))

def f(x):
    return eval(ecuacion, {'x' : x})

i = 0
fa = f(aValor)
fb = f(bValor)

while i <= maximoIteraciones:
    cValor = (aValor + bValor)/2
    fc = f(cValor)
    print"t%.4ftt%.4ftt%.4ftt%.4ftt%.8ft%.4f" % (aValor, bValor, fa, fb, cValor, fc)

    if (fc == 0.0) or abs(fc) < tolerancia:
        print "La raíz buscada es: %.8f" %cValor, "con " + str(i) + " iteraciones"
        break

    i = i +1

    if ((fa*fc) or maximoIteraciones):
        print "La raíz buscada es: %.8f" %cValor, "con " + str(i-1) + " iteraciones"
        break
