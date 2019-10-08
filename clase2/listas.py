#Declarando listas
vacio = []#Lista vacia, se le puede meter elementos despues
supermercado =["Lechuga","Crema","Pan"]#Lista de strings
edades = [10,45,60]#lista de numeros
mixto = ["Lechuga",10,4.5,"Pan"]#Lista de varios tipos de dato, no se recomienda mezclar datos
#Accediendo a la lista
print(edades[0])#Primer elemento de edades
print(supermercado[1])#Segundo elemento de supermercado
print(mixto[3].upper())#Cuarto elemento de la lista en mayusculas
#Modificando los elementos de la lista
peliculas = ["Django","Perros de reserva"]
print(peliculas[1])
peliculas[1] = "Había una vez en Hollywood"
print(peliculas[1])
#Añadiendo elementos
actores = []
actores.append("Brad Pitt")#Agrega al final el elemento 
print(actores[0])
actores.insert(0,"Jaime Fox")#Agrega el elemento en el numero que le das 
print(actores[0]+", "+actores[1])
#Eliminando elemnetos de la lista
musicos = ["José José","Juan Gabriel","Roger Waters","Paul McCartney","David Bowie"]
del musicos[1]#Elimina a Juan Gabriel de la lista
star_man=musicos.pop()#Elimina el último elemento de la lista y te lo da
print(star_man)
el_principe = musicos.pop(0)#Elimina el elemento del numero que brindas de la lista y te lo da
print(el_principe)
musicos.remove("Roger Waters")#Elimina el elemento que recibe como parametro
#Ordenar
numeros = [5,4,3]
numeros.sort()
print(numeros[0])
#Reversa
directores = ["Tarantino","Cameron"]
directores.reverse()
print(directores[0])
#Slices
jokers = ["Nicholson","Ledger","Leto","Phoenix"]
print(jokers[1:3])#Mostrara elementos de la lista del 1 al 2
print(jokers[1:4:2])#Mostrara los elementos del 1 al 3 moviendose de dos en dos
#Omitir elementos con slices
batmans = ["Affleck","Keaton","Bale"]
print(batmans[:2])#Solo va a imprimir del 0 al 1
print(batmans[1:])#Solo va a imprimir del 1 en adelante
#Matrices
matriz = [
    [1,2],
    [3,4]
]#La matriz es una lista de listas
d1 = matriz[0][0]*matriz[1][1]
d2 = matriz[0][1]*matriz[1][0]
determinante = d1 - d2
print(determinante)