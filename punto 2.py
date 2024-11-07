print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("-----------Actividad 2-----------")
cal = int(input("En una escala del 1 al 10 cual es tu calificasion?:"))#capturas el valor
SUSPENSO = cal <= 4#creas variables
SUFICIENTE = cal >= 5
BIEN = cal >= 7
NOTABLE = cal >= 9
SOBRESALIENTE = cal == 10
if SUSPENSO:#hases una cadena de if con cada una de esas variables con un mensaje difere
    print("estas suspendido idiota")
elif SUFICIENTE:
    print("suficiente pero repugnate")
elif BIEN:
    print("bien")
elif NOTABLE:
    print("esto es notable, te felisito")
elif SOBRESALIENTE:
    print("eres sobresaliente sige hasi")
else:#si fallas te insuta
    print("idiota no sabes calificar No sabe calificar")#cuando asia esto el programa relleno la respuesta despues del 
#idiota, escribio lo demas hasta donde dicer calificar
print("--------------------------------------")
print("Resultado: al se calificado se disne las verdades, y los pedido de la actividad\n")
