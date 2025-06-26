
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
vehiculos={
        1: {"marca": None, "año": None, "patente": None, "tipo": None},
        2: {"marca": None, "año": None, "patente": None, "tipo": None},
        3: {"marca": None, "año": None, "patente": None, "tipo": None},
        4: {"marca": None, "año": None, "patente": None, "tipo": None},
        5: {"marca": None, "año": None, "patente": None, "tipo": None}
    }

def ingresar_patente():
    minus=0
    mayus=0
    digito=0    
    while True:
        patente=input("Ingrese la patente a registrar)")
        for i in patente:
            if i.islower():
                minus+=1
            if i.isupper():
                mayus+=1
            if i.isdigit():
                digito+=1
        if minus == 4 and mayus == 0 and digito == 2 and len(patente) == 6:
            print("Patente ingresada correctamente.")   
            for k in vehiculos:
                if vehiculos[k][patente] is None:
                    vehiculos[k]["patente"] = patente
                
                print(f"Patente añadida en la posición {k}")
                break
            return patente
        else:
            print("Error al ingresar la patente. Debe tener 4 letras minúsculas y 2 dígitos, totalizando 6 caracteres.")
def ingresar_año():

        
        

    








