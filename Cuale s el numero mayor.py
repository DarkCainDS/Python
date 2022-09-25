print("/////////////////////////////")
print("Resolucion de numeros enteros")
print("/////////////////////////////")

numero_1 = int(input("\nIntroducir el primer numero entero:"))
numero_2 = int(input("\nIntroducir el segundo numero entero:"))
numero_3 = int(input("\nIntroducir el tercer numero entero:"))

if numero_1 > numero_2 and numero_1 > numero_3:
    print("\nEl numero mayor es",numero_1)
elif numero_2 > numero_1 and numero_2 > numero_3:
    print("El numero mayor es",numero_2)
else :
    print("\nEl numero mayor es",numero_3)
