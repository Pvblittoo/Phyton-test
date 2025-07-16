
# '''
# Crear gestion de vehiculos
# Crear programa para un parking de autos
# se debe ingresar
# Marca, año, patente, Tipo

# Marca: tipo string, se debe tipear la marca
# año: tipo int , solo de 4 digitos enteros
# patente: debe tener 4 letras minusculas y 2 digitos
# tipo: S= sedan, C= Camioneta, M= moto

# Se deve validar cada aspecto y tener un mantenedor para 
# todos los vehiculos motorizados

# 1.- Ingresar Vehiculo
# 2.- Mostrar Vehiculos
# 3.- Actualizar Vehiculo
# 4.- Borrar Vehiculo
# 5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
# 6.- Salir

# Usar dunciones con argumentos para poder validar
# y para poder llamar las acciones dentro del menu
Parking={}
lista_autos=["sedan","moto","camioneta"]
num_vehiculo=1
def cero_autos(total):
    if len(total)==0:
        print("no hay vehiculos actualmente en el parking")

def mostrar_vehiculos():
    for key,value in Parking.items():
        print(key,value)

def ingresa_año_vehiculo():
    while True:
        try:
            año=int(input("ingrese el año del vehiculo"))
            if len(str(año))==4:
                print("año ingresado con exito")
                break
            else:
                print("ingrese 4 digitos porfavor")
        except Exception:
            ("ingrese un valor valido")
    return año

def ingresa_patente():
    while True:
        try:
            minusculas=0
            mayusculas=0
            digito=0

            patente=str(input("ingrese patente a registrar"))
            for i in patente:
                if i.islower():
                    minusculas+=1
                if i.isupper():
                    mayusculas+=1
                if i.isdigit():
                    digito+=1
            if minusculas==4 and mayusculas==0 and digito==2 and len(patente)==6:
                    print("patente registrada con exito")
                    break
            else:
                print("porfavor ingrese una patente valida")
        except Exception:
            print("ingrese un valor valido")
    return patente

def ingresa_tipo_vehiculo():
    while True:
        try:
            tipo_vehiculos=int(input("ingrese el tipo de vehiculo a ingresar" \
            "1.-SEDAN" \
            "2.-MOTO" \
            "3.-CAMIONETA"))-1
            tipo=lista_autos[tipo_vehiculos]
            print("su vehiculo se ha registrado con exito")
            break
        except Exception:
            print("ingrese un valor valido")
    return tipo

while True:
    try:
        hacer=int(input("""-----BIENVENIDO AL PERKIN-----
                        -----¿QUE DESEAS HACER?-----
                        --1.-INGRESAR VEHICULO--
                        --2.-MOSTRAR VEHICULOS--
                        --3.-ACTUALIZAR VEHICULOS--
                        --4.-BORRAR VEHICULO--
                        --5.-MOSTRAR ESTADISTICAS DEL PERKIN=
                        -ULTIMO VEHICULO INGRESADO
                        -TOTAL EN GARAJE
                        --6.-SALIR--
                        """))
        match hacer:
            case 1:
                marca_nueva=str(input("ingrese la marca del vehiculo a registrar"))
                año=ingresa_año_vehiculo()
                patente=ingresa_patente()
                tipo=ingresa_tipo_vehiculo()
                Parking[num_vehiculo]={"Tipo":tipo,
                                       "Patente":patente,
                                       "Año":año,
                                       "Marca":marca_nueva}
                num_vehiculo+1
            case 2:
                if len(Parking)==0:
                    print("no hay vehiculos registrados")
                else:
                    mostrar_vehiculos()
            case 3:
                if len(Parking)==0:
                    print("no hay vehiculos para actualizar")
                else:
                    mostrar_vehiculos()
                    while True:
                        try:
                            vehiculo_actualizar=int(input("seleccione el vehiculo a actualizar"))
                            if vehiculo_actualizar in Parking:
                                while True:
                                    try:
                                        
                                        opc=int(input("ingrese una opcion" \
                                        "1.-editar" \
                                        "2.-salir"))
                                        match opc:
                                            case 1:
                                                nuevos_datos=int(input("""---¿QUE DATO DESEA ACTUALIZAR?---
                                                                    1.-TIPO
                                                                    2.-PATENTE
                                                                    3.-AÑO
                                                                    4.-MARCA
                                                                    
                                                                    """))
                                                match nuevos_datos:
                                                    case 1:
                                                        tipo=ingresa_tipo_vehiculo()
                                                        Parking[num_vehiculo]["Tipo"]=tipo
                                                        break
                                                    case 2:
                                                        patente=ingresa_patente()
                                                        Parking[num_vehiculo]["Patente"]=patente
                                                        break
                                                    case 3:
                                                        año=ingresa_año_vehiculo()
                                                        Parking[num_vehiculo]["Año"]=año
                                                        break
                                                    case 4:
                                                        marca=str(input("Ingrese la nueva marca"))
                                                        Parking[num_vehiculo]["Marca"]=marca
                                                        break
                                                    
                                                    case _:
                                                        print("ingrese un valor valido ")
                                            case 2:
                                                print("volviendo al menu principal")
                                                break 
                                                    
                                    except Exception:
                                        print("ingrese un valor valido")
                            else:
                                        break
                                        
                                        
                        except Exception:
                            print("ingrese un valor valido")
            case 4:
                if len(Parking)==0:
                    print("no hay vehiculos para eliminar")
                else:
                    mostrar_vehiculos()
                    while True:
                        try:
                            eliminar_vehiculo=int(input("ingrese vehiculo a eliminar"))
                            if eliminar_vehiculo in Parking:
                                del Parking[eliminar_vehiculo]
                                print("vehiculo eliminado")
                                break
                            else:
                                print("ingrese un vehiculo valido")
                        except Exception:
                            print("ingrese un valor valido")
            case 5:
                if len(Parking)==0:
                    print("no hay vehiculos para mostrar")
                else:
                    print(f"el ultimo vehiculo ingresado fue{Parking[num_vehiculo]} y el total de vehiculos en garaje es{len(Parking)}")
            case 6:
                print("saliendo...")
                break
    except Exception:
        print("ingrese un valor valido")


                    










                








        
        




        
        

    








