print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("-----------Actividad 3-----------")
name = str(input("Escoje un Nombre: "))
ap = str(input("Allade un Apellido: "))#capturar nombres

if name in "Daniel".lower():#haser cadena para preguntar por el nombre
    if ap in "Ramos".lower():#haser otra cadena de if dentro de otra, que pregunte por el apellido
        print("Nombre y apellido correctos.")
    else:
        print("Apellido incorrecto.")
else:#si en cualquiera de ambas es falso, maracara el mensaje
    print("Usuario desconocido.")#tranquilo la actividad es muy ambigua.
print("--------------------------------------")
print("Resultado: Si se las estrellas se aliena para dar el apellido y nombre corepto se bera si es el ususario corepto.\n")
