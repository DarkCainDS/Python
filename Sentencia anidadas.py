print("=========")
print("Conversor")
print("=========")

print("menu de opciones:\n")
print("Presiona 1 para convertir de numero a palabra.")
print("Presiona 2 para convertir de palabra a numero.")

opcion= int(input("\n Cual es tu opcion deseada?:"))

if opcion == 1:
    print("\n Conversor de numero a palabra")
    
    opcion_1 = int(input("\n Cual es el numero que deseas convertir a palabra:\n"))
    
    if opcion_1 == 1:
        print("El numero es {uno}")
    elif opcion_1 == 2:
        print("El numero es {dos}")
    elif opcion_1 == 3:
        print("El numero es {tres}")
    elif opcion_1 == 4:
        print("El numero es {cuatro}")
    else:
        print("El numero no esta registrado ")
        
elif opcion ==2:
    print("\n Cual es la palabra que deseas convertir:\n")
    
    opcion_2=(input("Palabra a convertir en numero:"))
    opcion_2 = opcion_2.lower()
    if opcion_2 == "uno":
        print("el numero es 1")
    elif opcion_2 == "dos":
        print("El numero es 2")
    elif opcion_2 == "tres":
        print("El numero es 3")
    elif opcion_2 == "cuatro":
        print("El numero es 4")
    elif opcion_2 == "cinco":
        print("El numero es 5")
    else:
        print("opcion no disponible")
else:
        print("opcion no disponible")
print("Fin.")



