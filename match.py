def suma():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la suma es " ,n1+n2)

def rests():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la resta es ",n1-n2)

def divi():
    try:
        n1=int(input("ingrese un numero"))
        n2=int(input("ingrese otro numero"))
        print("el resultado de la   division es ",n1/n2)
    except ZeroDivisionError as nombre_de_excepcion:
        print(f"Se produjo una excepción: {nombre_de_excepcion}")
  

def multi():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la multiplicacion es",n1*n2)

def calcu ():
    while True:
        try:
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
        except Exception :
            print("no se puede ingresar caracteres")

a=int(input("desea ocupar la calculadora 1.si 2.no"))

if a ==1:
    calcu()






   