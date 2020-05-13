import math
pi = math.pi
n=0
x= pi/6 + 2*pi
senox=0
factorial = 1
contador=1
error = 5

while (abs(error) >= 0.001):
		
	while (contador <= 2*n+1):
		factorial = factorial * contador	
		contador = contador + 1
		nuevo_termino=((-1)**n * x**(2*n+1)) / (factorial)
	senox= senox + nuevo_termino
	error= senox - 0.5
	n=n+1
	factorial=1
	contador=1
print n, senox
	
