#Ejercicio 1 imprimir nombre mas de una vez en diferentes lineas  (Solucion)
nombre=input("Ingrese su nombre")
numero= (input("ingrese un numero"))
print((nombre + "\n") * int((numero)))

#Ejercicio 2 imprimir el nmobre en mayus, minus,y la primera letra mayus   (Solucion)
name= input("Cual es tu nombre completo: ")
print(name.lower())
print(name.upper())
print(name.title())

#Ejercicio 3 preguntar nombre de usuario y letras   (Solucion)
nombre3= input("Cual es tu nombre")
print(nombre3.upper() + "tiene" + str(len(nombre3)) + "Letras")

#Ejercicio 4 escribir un programa quitando el inicio y el final (Solucion)
tel=input("Introduce tu numero de telefono con el formato +56-xxxxxxx-xx:")
print("El numero de telefono es ", tel[4:-2])

#Ejercicio 5  iniciar un programa que devuelva la palabra invertida (Solucion)
oracion= input("Introduce una oración")
print(oracion[::-1])

#Ejercicio 6  (Solucionado)(-) (Solucion)
frase_6=input("Introducir una frase:")
vocal_6=input("Introducir una vocal:")
print(frase_6.replace(vocal_6,vocal_6.upper()))

#Ejercicio 7 (Solucion)
correo_7=input("Introducir corre electronico")
print(correo_7[:correo_7.find("@")] + "@ceu.es")

#Ejercicio 8  (Solucionado)
precio_8=input("Precio de un vaso con dos decimales:")
print(precio_8[:precio_8.find(".")], "dolares", precio_8[precio_8.find(".")+1:], "Centavos")
#Ejercicio 9 (Solucion)
fecha= input("Introduce la fecha de nacimiento en formato dd/mm/aaaa :")
print("dia", fecha[:2])
print("mes", fecha[3:5])
print("año", fecha[6:])
dia=fecha[:fecha.find("/")]
mesaño= fecha[fecha.find("/")+1:]
mes=mesaño[:mesaño.find("/")]
año= mesaño[mesaño.find("/")+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)
# Ejercicio 10   (Solucion)
canasta=input("Introduce los productos de la cesta de la compra separado por comas:")
print(canasta.replace(",", "\n"))
canasta=input("Introduce los productos de la cesta de la compra separado por comas:")
print("\n".join(canasta.split(",")))

#Ejercicio 11  (Solucion)
producto= input("Introduce el nombre del producto:")
precio= float(input("Introducir el precio unitario:"))
unidades= int(input("introduce el numero de unidades:"))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))              
print('{unidades:3d}')
