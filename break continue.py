#ejemplo de break#

print("while con la sentencia break \n")
contador= 0
while contador <10:
    contador+=1

    if contador == 5:
        break
    print("valor de contador es:", contador)

print("fin del programa . break iniciado")

#ejemplo continue#
print("\nwhile con la sentencia break \n")
contador= 0
while contador <10:
    contador+=1

    if contador == 1:
        continue
    elif contador == 2:
        continue
    print("valor de contador es:", contador)

print("fin del programa . continue iniciado")
