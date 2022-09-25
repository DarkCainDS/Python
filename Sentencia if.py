nombre = input("Introduce tu nombre :")
matematica = float(input(nombre + " Nota en Matematica :"))
quimica = float(input(nombre + " Nota en quimica :"))
biologia = float(input(nombre + " Nota en Biologia :"))
Resultado = (matematica + quimica + biologia)/3
print(Resultado)
if Resultado>=4:
    print(" Felicidades", nombre, "Aprobaste con nota" , Resultado)

else:
     print("Lamentamos informarle", nombre ," reprobaste con nota",  Resultado)
print("Fin")
