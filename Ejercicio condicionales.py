#Ejercicio 1 preguntar por edad y monstrar por pantalla si es mayor de edad (Solucionado)
edad=int(input("Ingresa tu edad: "))
if edad >=18 :
    print("Eres mayor de edad")
else :
    print("Eres menor de edad")
# Ejercicio 2 almacenar contraseña y monstrarla sin impor mayus o minus (solución)
contraseña = "contraseña"
password=input("Introduce la contraseña")
if contraseña == password.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")
# Ejercicio 3 mostrar una división  (Solucionado)
numero1=int(input("Ingresar un numero entero:"))
numero2=int(input("Ingresar otro numero entero:"))
if numero1 and numero2 == 0 :
    print("Ha ocurrido un error , volver a intentarlo")
else :
    print((numero1 / numero2))
#Ejercicio 4 mostrar si un numero es par o impar (Solucionado)
numero_4=int(input("Ingresar un numero entero"))
resultado= numero_4 % 2
if resultado == 0 :
    print("El numero es par")
if resultado == 1 :
    print("El numero es impar")
#Ejercicio 5   (Solucionado)
edad_5=int(input("Ingresar edad del contribuyente:"))
ingreso_5= int(input("Ingresar los ingresos del contribuyente:"))
if edad_5 >=16 and ingreso_5 >=1000 :
           print("Debes cotizar ")
else :
    print("No debes cotizar")
           
#Ejercicio 6 dividir por nomber y genero   (Solución)
nombre_6= input("Ingresar tu nombre")
genero_6= input("Cual es tu sexo(H o M)?")
if genero_6 == "M" :
    if nombre_6.lower() < "m":
        grupo= "A"
    else:
        grupo="B"
else :
    if nombre_6.lower() >"n":
        grupo = "A"
    else :
        grupo = "B"
print("Tu grupo es " + grupo)

#Ejercicio 7 impositivo  (Solucionado)
ingreso_7= int(input("Ingrese su renta anual"))
if ingreso_7 < 10000 :
    impuesto_1=5
    print(ingreso_7 , "Su cargo impositivo es del 5%y el total a pagar es",(ingreso_7 * impuesto_1)/100, "$")
elif ingreso_7 >= 10000 and ingreso_7 < 20000 :
    impuesto_2=15
    print(ingreso_7 , "Su cargo impositivo es del 15%y el total a pagar es",(ingreso_7 * impuesto_2)/100,"$")
elif ingreso_7 < 20000 and ingreso_7 < 35000 :
    impuesto_3=20
    print(ingreso_7 , "Su cargo impositivo es del 20%y el total a pagar es",(ingreso_7 * impuesto_3)/100,"$")
elif ingreso_7 < 35000 and ingreso_7 < 60000 :
    impuesto_4=30
    print(ingreso_7 , "Su cargo impositivo es del 30%y el total a pagar es",(ingreso_7 * impuesto_4)/100,"$")
elif ingreso_7 >= 60000 :
    impuesto_5=45
    print(ingreso_7 , "Su cargo impositivo es del 45% y el total a pagar es",(ingreso_7 * impuesto_5)/100,"$")
#Ejercicio 8 (copy y paste) no entender el problema
bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))
# Clasifiación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))

#Ejercicio  ingresar un programa que diga el valor de la entrada (Solucionado)
persona_9=int(input("Ingrese su edad:"))
if persona_9 <= 4 :
    print("La entrada es gratis")
elif persona_9 >4 and persona_9 < 18 :
    print("La entrada cuesta 5$")
elif persona_9 > 18 :
    print("La entrada es cuesta 10$")

#Ejercicio 10   (Solucionado) + (Solucion)
print("Bienvenido a la pizzeria bella napoli")
tipodepizza=input("Desea ordenar una pizza vegetariana?")
if tipodepizza == "si".lower() :
    print("Los ingredientes vegetarianos son: tofu y pimiento")
    ingrediente = input("elegir entre los ingredientes vegetarianos:")
    if ingrediente == "tofu".lower() :
        print("su pizza vegetariana contiene mozzarella tomate y tofu")
    elif ingrediente == "pimiento".lower() :
        print("su pizza vegetariana contiene mozzarella tomate y pimiento")
    else :
        ingrediente == ""  
        print("Opcion invalida intentarlo de nuevo")
else:
    tipodepizza == "no".lower() 
    print("Los ingredientes carnicos son: pepperoni , jamon, salmon")
    ingrediente_1 = input("elegir entre los ingredientes carnicos:")
    if ingrediente_1 == "pepperoni".lower() :
        print("su pizza carnica contiene mozzarella tomate y pepperoni")
    elif ingrediente_1 == "jamon".lower() :
        print("su pizza carnica contiene mozzarella tomate y jamon")
    elif ingrediente_1 == "Salmon".lower() :
        print("su pizza carnica contiene mozzarella tomate y salmon")
    else :
        ingrediente_1 == " " 
        print("Opcion invalida intentarlo de nuevo")
print("Su pedido se preparara a la brevedad.")

#presentacion de opciones#
print("Bienvenido a la pizzeria Bella Napoli.\n tipos de pizza \n \t1- Vegetariana\n\t2- No vegetariana\n")
tipo=input("Introduce el numero correspondiente al tipo de pizza que quieres:")      
#decision de la pizza#
if tipo == "1" :
    print("Ingredienties de pizza vegetarianas\n\t1 pimiento\n\t2- Tofu\n")
    ingrediente= input("introduce el ingrediente que deseas:")
    print("Pizza vegetariana con mozzarekka , tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else:
        print("tofu")
else:
    print("Ingredientes de pizza no vegetarianas\n\t1- pepperoni\n\t2- Jamón\n\t3-Salmón\n")
    ingrediente= input("introduce el ingrediente que deseas:")
    print("Pizza no vegetariana con mozarella,tomate y ", end="")
    if ingrediente == "1" :
        print("pepperoni")
    elif ingrediente == "2" :
        print("Jamon")
    else :
        print("Salmón")

    
        
