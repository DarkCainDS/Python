print("===================================")
print("Solicitud de vacaciones disponibles")
print("===================================")

nombre = input("Introducir nombre del trabajador:")
clave = int(input("Ingresar clave del trabajador:"))
años = float(input("Ingresar años de servicio:"))

if clave == 1 and años == 1:
    print("Al trabajador le corresponden 6 dias de vacaciones")
elif clave == 1 and años >=2 and años <=6 :
    print( nombre, "le corresponden 14 dias de vacaciones")
elif clave == 1 and años >=7:
    print( nombre, "le corresponden 20 dias de vacaciones")
elif clave ==1 and años <1:
    print("Sin derecho a vacaciones")

if clave == 2 and años == 1:
        print("al trabajador le corrresponden 7 dias de vacaciones")
elif clave == 2 and años >=2 and años <=6 :
    print( nombre, "le corresponden 15 dias de vacaciones")
elif clave == 2 and años >=7:
    print( nombre, "le corresponden 21 dias de vacaciones")
elif clave == 2 and años <1:
    print("Sin derecho a vacaciones")

if clave == 3 and años == 1:
        print("al trabajador le corrresponden 10 dias de vacaciones")
elif clave == 3 and años >=2 and años <=6 :
    print( nombre, "le corresponden 20 dias de vacaciones")
elif clave == 3 and años >=7:
    print( nombre, "le corresponden 30 dias de vacaciones")
elif clave == 3 and años <1:
    print("Sin derecho a vacaciones")

if clave >3 or clave == 0:
    print("La clave no existe")
    
print("Fin")
