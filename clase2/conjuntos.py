#Declarando 
odds = {1,2,3,5,7}
odds.add(11)
#Union
personajes_lotr = {"Legolas","Gandalf","Frodo","Sam","Aragorn"}
personajes_got = {"Jon","Cersei","Jaime","Tyrion","Sam"}
personajes_ficticios = personajes_lotr.union(personajes_got)
print(personajes_ficticios)
#Intersección
personajes_repetidos = personajes_lotr.intersection(personajes_got)
print(personajes_repetidos)
#Diferencia
personajes_originales = personajes_got.difference(personajes_lotr)
print(personajes_originales)
#Removiendo elementos
personajes_got.remove("Jaime")#Si no encuentra el elemento manda error
personajes_got.discard("Cersei")#Si no encuentra el elemento no pasa nada y el conjunto se queda igual
print(personajes_got)