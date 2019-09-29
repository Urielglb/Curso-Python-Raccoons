#Pedir nombre y dar división entera
nombre = input("Hola,¿Como te llamas?\n")
dividendo = input("Dame un dividendo\n")
divisor = input("Dame un divisor\n")
resultado = float(dividendo)//float(divisor)
residuo = float(dividendo)-((divisor)*resultado)
print(nombre + " el resultado entero de " + dividendo + "/" + divisor + " es " + str(resultado) + " y el residuo es "+ str(residuo))
#Frase de película
