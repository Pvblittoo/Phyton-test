#pida al usuario la cantidad de perros muestre cual es la cuota minima de conejos luego consulte cuantos conejos trajo si el perro trajo la cantida minima de conejos cumplio la cuota ,si no ,se queda sin filete mostrar resumen de perro que cumplieron y los que no
import random

perros=int(input("Cuantos perros desea enviar a cazar"))
cumplen=0
cmconejos=10

while True:
        try:
            perros=int(input("Cuantos perros desea enviar a cazar"))
            cumplen=0
            cmconejos=10
            for p in range (perros):
                cantconejoscazados=random.randint(0,20)
                if cantconejoscazados>=cmconejos:
                    print(f"el perro {p+1} cumplio la cuota")
                    cumplen=cumplen+1
                else:
                    print (f"el perro {p+1} se queda sin filete")
            print("el total de perros que cumplio la cuota fue ",(cumplen))
            print("el total de perros que no cumplen es ",perros-cumplen)
        except Exception:
             print("solo puede ingresar numero")



    
                           
    




