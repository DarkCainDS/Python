print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Programa para determinar si un numero es par o impar")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

numero_entero= int(input("\n introducir un numero entero:"))
resultado= numero_entero % 2
if resultado == 0:
                   print(" \n El numero es par")
elif resultado == 1:
                   print("El numero es impar")
