def suma():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la suma es " ,n1+n2)

def rests():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la suma es " ,n1-n2)

def divi():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la suma es " ,n1/n2)

def multi():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la suma es " ,n1*n2)

def calcu ():
    while True:
        op=int(input("que prefiero:1.suma 2.resta 3.division 4.multilicar 5. salir "))

        match op:
            case 1: 
                print("suma")
                suma()
            case 2:
                print("resta")
                rests()
            case 3:
                print("division")
                divi()
            case 4:
                print("multiplicacion") 
                multi()
            case 5: 
                print("salir")
                break






   