from math import sin as senopy

def factorial(numero):
	factorial = 1
	while (numero > 1):
	    factorial = factorial * numero
	    numero = numero - 1
	return factorial

def seno_taylor(x, precision=20) :    
	sum_seno = 0.0
	n = 0.0
	termino = 1.0
	while (n < precision) :
	    termino = ((x**(2*n))) / (factorial (2*n))
	    if (n % 2 == 0):
		sum_seno = sum_seno + termino
	    else:
		sum_seno = sum_seno - termino
	    n = n + 1
	return sum_seno

def prueba_seno_taylor(x, precision=20):
	a = 0
	print ("sin(x) ".rjust(20) + "error verdadero".rjust(20) + "error porcentual".rjust(20))
	while (a < precision):
	    seno = seno_taylor(x,a)
	    error = senopy(x) - seno
	    error_porcentual = error / senopy(x) * 100
	    print (str(seno).rjust(20)) + str(error).rjust(20) + str(error_porcentual).rjust(20)
	    a = a + 1

prueba_seno_taylor(2)
