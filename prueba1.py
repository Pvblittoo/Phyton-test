nombres = ["Juan", "Ana", "Pedro"]
apellidos = ["Pérez", "Gómez", "Martínez"]

# Método 1: Operador +
nombres_y_apellidos = nombres + apellidos

# Método 2: Método extend()
nombres_y_apellidos = []
nombres_y_apellidos.extend(nombres)
nombres_y_apellidos.extend(apellidos)

# Unir la lista en una cadena con espacios
cadena = " ".join(nombres_y_apellidos)

print(cadena)