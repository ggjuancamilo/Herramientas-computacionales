#!/usr/bin/python

class HookeandoAndo:
	'Se calculara la fuerza de un resorte'
	g=9.8 #aceleracion gravitacional
	def __init__(self, y0, Vy0, m0, k0):
		self.y=y0
		self.Vy=Vy0
		self.m=m0
		self.k=k0


	def calculaFuerza(self):
		self.Fy=-self.y*self.k


	def muevete(self, dt):
		self.y+=self.Vy*dt
		self.Vy+=dt*self.Fy/self.m
 

	def imprime(self, t):
		print t, self.Fy

Resorte=HookeandoAndo(3, 1, 3, 2)
Resorte.calculaFuerza()
t=0.0
Deltat=0.001
while t<10.0:
	print t, getattr(Resorte, 'y')  #Resorte.imprime(t)
	Resorte.muevete(Deltat)
	Resorte.calculaFuerza()
	t+=Deltat 


