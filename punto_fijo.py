from math import *

def f(x):
	return eval(ecuacion, {'x' : x})

ecuacion = raw_input('Ingrese la funcion a resolver: ')
p0=float(raw_input('Introduce el valor de inicio p0: '))
tol=float(raw_input('Introduce el error '))
n0=int(input('Ingrese el maximo de iteraciones a realizar: '))
i=1

while i<=n0:
	p=f(p0)
	if abs(p-p0)<tol:
		print("El punto fijo es ",p," despues de ",i," iteraciones")
		break
	i=i+1
	p0=p
	if i>n0:
		print "El metodo no converge "
		break
