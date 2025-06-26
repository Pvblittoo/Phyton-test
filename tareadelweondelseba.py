# pida al usuario que cree un nombre este debe tener 2 mayusculas 2 minusculas y 2 digitos ademas de que debe tener 7 carateres


mayus=0
minus=0
digito=0

nmbres={
    1:{"usuario1":None},
    2:{"usuario2":None},
    3:{"usuario3":None}
    }

while True:
    op=int(input("ingrese lo que desea realizar:" \
    "1.-añadir nombre" \
    "2.-ver nombres añadidos" \
    "3.-editar nombre" \
    "4.-eliminar nombre" \
    "5.-salir"))
    match op:
        case 1:
            nombre=(input("ingrese su nombre a crear"))
            for i in nombre:
                if i.islower():
                    minus+=1
                if i.isupper():
                    mayus+=1
                if i.isdigit():
                    digito+=1
            if digito==2 and mayus==2 and minus==2 and len(nombre)==7:
                print("su nombre ah sido validado")
                nmbres[1]=nombre
                break
            else:
                print("pone la wea denuevo shushetumare")
        case 2:
            print(nmbres)
        case 5:
            print("saliendo")
            break


  

