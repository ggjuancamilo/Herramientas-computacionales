

infile = open("Romeo_and_Juliet.txt", "r") #Abre el archivo
milista=infile.readlines() # lista donde cada elemento es un renglon
romeo=0
julieta=0
for ddd in milista:
	renglon = ddd.split()	# convierte cada elemento de milista en una lista de las palabras que hay en el renglon
	for var in renglon:
		romeo = romeo + var.count("Romeo") + var.count("ROMEO") #cuenta en cada renglon cuantas veces esta Romeo y las adiciona a la variable romeo


for ddd in milista: 
	renglon = ddd.split()	
	for var in renglon:
		julieta = julieta + var.count("Juliet") + var.count("JULIET")


print "En el texto encontramos ", romeo, " veces Romeo."

print "En el texto encontramos ", julieta, " veces Juliet"
