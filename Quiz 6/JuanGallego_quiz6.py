def MCD(a,b):
	if a<0 | b<0: print "retrasado, deben ser mayores a cero" 
	elif a==0 : return b
	elif b==0: return a 
	elif a>b:
 		if a%b ==0: return b
		else: return MCD(b,a%b)
	elif a<=b:
		if b%a == 0: return a
		else: return MCD(a,b%a)
	
print MCD(1071,-462)
