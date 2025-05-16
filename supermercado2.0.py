

cant=int(input("Cuantos productos desea llevar?"))
total=0
tt=0

def frutas ():
    print("valores platano=600 frutillas=500 sandia=1000 naranja=500")
    for i in range (cant):
            print("""
                1.Platanos
                2.Frutillas 
                3.sandia
                4.naranja""")
            op=int(input("Que desea llevar"))
            if op==1:
                print("usted lleva platanos")
                total=total+600
            if op==2:
                print("usted lleva frutillas")
                total=total+500
            if op==3:
                print("usted lleva sandia")
                total=total+1000
            if op==4:
                print("usted lleva naranja")
                total=total+500
    return total

def verduras():
    print("valores limon=600 tomate=500 papa=1000 cebolla 500")     
    for i in range (cant):
        print("""
                      1.limon
                       2.tomate
                      3.papa
                       4.cebolla""")
        op=int(input("Que desea llevar"))
        if op==1:
            print("usted lleva limon")
            total=total+600
        if op==2:
            print("usted lleva tomate")
            total=total+500
        if op==3:
                print("usted lleva papa")
                total=total+1000
        if op==4:
            print("usted lleva cebolla")
            total=total+500 
    return total
def lacteos():
    print("valores leche=600 yogurth=500 queso=1000 mantequilla=500 ")
    for i in range (cant):
                print("""
                      1.leche
                       2.yogurth 
                      3.queso
                       4.mantequilla""")
                op=int(input("Que desea llevar"))
                if op==1:
                    print("usted lleva leche")
                    total=total+600
                if op==2:
                    print("usted lleva yogurth")
                    total=total+500
                if op==3:
                     print("usted lleva queso")
                     total=total+1000
                if op==4:
                    print("usted lleva mantequilla")
                    total=total+500
    return total

def abarrotes():
    print("valores tallarines=600 fideos=500 arroz=1000 porotos=500")
    for i in range (cant):
        print("""
                      1.tallarines
                       2.fideos
                      3.arroz
                       4.porotos""")
    op=int(input("Que desea llevar"))
    if op==1:
        print("usted lleva tallarines")
        total=total+600
    if op==2:
        print("usted lleva fideos")
        total=total+500
    if op==3:
        print("usted lleva arroz")
        total=total+1000
    if op==4:
        print("usted lleva porotos")
        total=total+500
    return total

def supermercado():
    while True:
        tt=0
        op=int(input("""que desea comprar
                    1.frutas
                    2.verduras
                    3.lacteos
                    4.abarrotes"""))
        match op:
            case 1 :
                print("frutas")
                tt=tt+frutas()
            case 2:
                print("verduras")
                tt=tt+verduras()
            case 3:
                print("lacteos")
                tt=tt+lacteos()
            case 4:
                print("abarrotes")
                tt=tt+abarrotes()
        return total 
ingresar=int(input("desea ingresar al supermercado 1.si 2.no"))
if ingresar==1:
    supermercado()


                

                    
                    
      
      
        
      


      

                    




