##Entradas
ec = raw_input("Ecuacion: ")
x0 = float(raw_input("x0: "))
x1 = float(raw_input("x1: "))
 
##Metodo
f0 = eval(ec, {'x' : x0})
f1 = eval(ec, {'x' : x1})
tol = 0.00001
max_iter = 10
 
if f0 * f1 < 0.0:
    Ea = 0
    R = x1 - (f1 * (x0 - x1)) / (f0 - f1)
    while abs((x1 - x0) / x1) > tol and max_iter > 0:
	Ea = R
	R = x1 - (f1 * (x0 - x1)) / (f0 - f1)
        fR = eval(ec, {'x' : R})
        if f0 * fR < 0.0:
            x1 = R
            f1 = fR
        if fR * f1 < 0.0:
            x0 = R
            f0 = fR
	max_iter = max_iter - 1
	ErpA = ((R - Ea)/R)*100
	print "Error relativo porcentual aproximado {0}".format(ErpA)
 
##Salidas
if f0 * f1 < 0.0:
    print "La raiz es:", R
else:
    print "Valores iniciales malos"
