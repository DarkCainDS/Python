#Ejercicio 1 mostrar palabra 10 en pantalla ##      (Solucionado) +(Solucion)
palabra_1 = "One Piece"
x=0
while x < 2 :
    x+=1
    print(palabra_1)
for i in range(2): 
    print(palabra_1)
#Ejercicio 2 preguntar edad y mostrar todos los años en pantalla    (Solucionado) + (Solucion)

edad_2=int(input("Intruducir edad del usuario"))
x=1
while not x > edad_2 :
    if x == 1:
        print( x ,"Año")
    else :
        print( x , "Años")
    x += 1
for i in range(edad_2):
    print("Has cumplido " + str(i+1) + " años")     ##i al ser un numero entero se pasa a str##

#Ejercicio 3 mostrar numeros impares del 1 hasta el input##     (Solucionado) + (Solucion)

numero_3=int(input("Ingresar un numero entero"))
x=1
while not x > numero_3 :
    print(x, end=",")
    x += 2
for i in range (1, numero_3 , 2): ##solucion paguina##
    print(i, end=",")

#Ejercicio 4 pedir numero entero y hacer cuenta regresiva   (Solucion)

numero_4=int(input("\nIngresar un numero entero positivo"))

for i in range ( numero_4,-1, -1):
    print(i ,end=",")

#Ejercicio 5 inversion+ interes anual+ años     (Solucion)
inversion=float(input("Cantidad a invertir"))
interes_anual=float(input("Interes anual"))
años=int(input("Cantidad de años"))
for i in range(años) :
      inversion *= 1 + interes_anual /100
      print("capital tras" + str(i+1) + "años" + str(round(inversion,2)))

#Ejercicio 6 triangulo de *
numero_6=int(input("Ingresar un numero entero"))

for i in range(numero_6):
    print("*"*(i+1))

#Ejercicio 7 tabla de multiplicar del 1 al 10 s(olucion)
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end="\t")
    print("")
#Ejercicio 8 triangulo con un numero entero (Solucion)
    numero_8=int(input("Ingresar un numero entero"))
for i in range(1,numero_8,2):
    for j in range(i,0,-2):
        print(j,end="")
    print("")

#Ejercicio 9 peticion de contraseña   (Solucion)
key="contraseña"
password=""
while password != key :
    password= input("Ingresar contraseña")
print("Contraseña correcta")

#Ejercicio 10 Numeros primos

numero_10=int(input("Ontroducir un numero entero positivo mayor que 2:"))
iteracion=2
while numero_10 % iteracion != 0:
    iteracion +=1
if iteracion == numero_10 : 
    print(str(numero_10) + "Es primo")
else :
    print(str(numero_10) + "No es primo")

#Ejercicio 11
