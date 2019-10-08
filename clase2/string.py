#String es un conjunto de caracteres y se puede trabajar como una lista
nombre = "Uriel"
print(nombre[2])#Imprime la tercer letra del string
print(nombre[2:])#Imprime desde la tercer letra
#Agregando valores
mensaje = "Hola, mi nombre es {} y tengo {} años".format("Uriel",19)#Agrega en orden
print(mensaje)
mensaje = "Hola, mi nombre es {1} y tengo {0} años".format(19,"Uriel")#Agrega según el numero que le indica
print(mensaje)
mensaje = "Hola, mi nombre es {first} y tengo {last} años".format(last =19,first ="Uriel")#Agregando por valores
print(mensaje)
#Split
numeros = "1,2,3,4,5"
lista_de_numeros = numeros.split()
print(lista_de_numeros)
#Join
numeros = ",".join(lista_de_numeros)
print(numeros)
#Encontrar cadena
celulares = "Iphone Samsung Huawei"
print(celulares.find("Samsung"))#Regresa el digito de donde esta la primera letra de la palabra a buscar
