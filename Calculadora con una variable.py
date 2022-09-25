print("Calculadora con una sola variable","\n")
print("****************")
print("Menu de opciones")
print("****************","\n")

print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")
print("5.División entera")
print("6.Exponente")
print("7.Modulo o resto","\n")

numero= int(input("Introduce la opcion deseada: "))
if numero == 1:
    print("Elegiste Suma")
    numero -= numero
    numero += int(input("Introduce el primer numero: "))
    numero += int(input("Introduce el segundo numero: "))
    print(numero)
elif numero == 2:
    print("Elegiste Resta")
    numero -= numero
    numero += int(input("Introduce el primer numero: "))
    numero -= int(input("Introduce el segundo numero: "))
    print(numero)
elif numero == 3:
    print("Elegiste Multiplicación")
    numero -= numero
    numero += int(input("Introduce el primer numero: "))
    numero *= int(input("Introduce el segundo numero: "))
    print(numero)
elif numero ==4:
    print("Elegiste División")
    numero -= numero
    numero += int(input("Introduce el primer numero: "))
    numero /= int(input("Introduce el segundo numero: "))
    print(numero)
elif numero == 5:
    print("Elegiste División entera")
    numero -= numero
    numero += int(input("Introduce el primer numero: "))
    numero //= int(input("Introduce el segundo numero: "))
    print(numero)
elif numero == 6:
    print("Elegiste Exponente")
    numero -= numero
    numero += int(input("Introduce el primer numero: "))
    numero **= int(input("Introduce el segundo numero: "))
    print(numero)
elif numero == 7:
    print("Elegiste Modulo o resto")
    numero -= numero
    numero += int(input("Introduce el primer numero: "))
    numero %= int(input("Introduce el segundo numero: "))
    print(numero)
else:
    print("esta opcion no Existe")




