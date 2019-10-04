#Declarando diccionarios 
peliculas_batman = {"Nolan":"The Dark Knight","Snyder":"Batman v Superman","Burton":"Batman regresa"}#Los diccionarios guardan un valor con una llave y para declaralo es llave : valor
print(peliculas_batman["Nolan"])
#Agregar valor
peliculas_batman["Reeves"] = "The Batman"
print(peliculas_batman["Reeves"])
#Borrando valores
del peliculas_batman["Snyder"]#Borra el elemento por su llave 
pelicula = peliculas_batman.pop("Burton")#Borra el elemento por su llave y regresa el valor que guardaba la llave
print(pelicula)
