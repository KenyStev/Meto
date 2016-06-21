#!/usr/bin/python
#-*- coding:utf-8 -*-
from math import *

def f(x):
    return eval(ecuacion, {'x' : x})
    
print "Método de la secante Mejorado"

ecuacion = raw_input('Ingrese la función a resolver: ')
x1 = float(raw_input('Introduce el valor de inicio x1: '))
epsilon = float(raw_input('Introduce el valor de inicio epsilon: '))
erroru=float(raw_input('Introduce el error '))
raiz=[]
raiz.insert(0,0)
i=0
error=1
while abs(error) > erroru:
    x2 = x1 - (epsilon*f(x1)*x1)/(f(x1 + epsilon*x1)-f(x1))
    raiz.append(x2)
    x1 = x2
    i = i+1
    error=(raiz[i]-raiz[i-1])/raiz[i]
    print x2
