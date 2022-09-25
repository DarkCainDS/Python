print("Conjunción (and)\n")
numero_uno = int(input("Escribe un numero mayor a 2 y menor a 5:"))

if numero_uno >= 2 and numero_uno <= 5:
                 print("\n El numero " , numero_uno , "es mayor a 2 o igual y menor que 5")
else:
    print("El numero", numero_uno , "No cumple con la condicion \n")

print(" \n Disyunción(or)\n")

palabra = input("Para cumplir la condicion escribe ’si’ o yes :")
palabra = palabra.lower()

if palabra == "si" or palabra == "yes":
    print(" \n La condicion se ha cumplido")
else:
    print("La condicion No se ha cumplido")

print("\n Negacion (Not)")

numero_dos= int(input("Introduce un numero igual a 5:"))

if not numero_dos == 5:
    print("El numero no es igual a cinco y no  cumple la condicion")
else :
    print("El numero es igual a cinco y cumple la condicion")
