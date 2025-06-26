nmbres = {
    1: {"nombre": None},
    2: {"nombre": None},
    3: {"nombre": None}
}

while True:
    op = int(input("\nIngrese lo que desea realizar:\n" \
                   "1.- Añadir nombre\n" \
                   "2.- Ver nombres añadidos\n" \
                   "3.- Editar nombre\n" \
                   "4.- Eliminar nombre\n" \
                   "5.- Salir\n" \
                   "Opción: "))
    
    match op:
        case 1:
            nombre = input("Ingrese su nombre a crear: ")
            mayus = minus = digito = 0  # Reiniciar contadores

            for i in nombre:
                if i.islower():
                    minus += 1
                if i.isupper():
                    mayus += 1
                if i.isdigit():
                    digito += 1

            if digito == 2 and mayus == 2 and minus == 2 and len(nombre) == 7:
                print("Su nombre ha sido validado.")

                # Buscar primer espacio disponible
                agregado = False
                for k in nmbres:
                    if nmbres[k]["nombre"] is None:
                        nmbres[k]["nombre"] = nombre
                        print(f"Nombre añadido en la posición {k}")
                        agregado = True
                        break
                if not agregado:
                    print("No hay espacio para más nombres.")
            else:
                print("Nombre inválido. Debe tener 2 mayúsculas, 2 minúsculas, 2 dígitos y 7 caracteres en total.")

        case 2:
            print("\nNombres guardados:")
            for k, v in nmbres.items():
                print(f"{k}: {v['nombre']}")

        case 3:
            pos = int(input("Ingrese la posición (1-3) a editar: "))
            if pos in nmbres:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nmbres[pos]["nombre"] = nuevo_nombre
                print("Nombre actualizado.")
            else:
                print("Posición inválida.")

        case 4:
            pos = int(input("Ingrese la posición (1-3) a eliminar: "))
            if pos in nmbres:
                nmbres[pos]["nombre"] = None
                print("Nombre eliminado.")
            else:
                print("Posición inválida.")

        case 5:
            print("Saliendo del programa.")
            break

        case _:
            print("Opción no válida.")
