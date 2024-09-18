# Preguntar al usuario qué tipo de vehículo desea
print("Bienvenido a la concesionaria. ¿Qué tipo de vehículo te interesa?")
print("1. Moto")
print("2. Auto")
tipo_vehiculo = input("Introduce el número del vehículo (1 para Moto o 2 para Auto): ").strip()

# Inicializar variables para el color
color = ""

# Mostrar opciones de colores y pedir al usuario que elija un color
if tipo_vehiculo == '1':
    print("Opciones de colores para Moto:")
    print("1. Rojo")
    print("2. Blanco")
    print("3. Negro")
    color_opcion = input("Introduce el número del color (1 para Rojo, 2 para Blanco o 3 para Negro): ").strip()

    if color_opcion == '1':
        color = 'Rojo'
    elif color_opcion == '2':
        color = 'Blanco'
    elif color_opcion == '3':
        color = 'Negro'
    else:
        print("Opción de color no válida para Moto.")
        color = 'Desconocido'

elif tipo_vehiculo == '2':
    print("Opciones de colores para Auto:")
    print("1. Gris")
    print("2. Azul")
    print("3. Amarillo")
    color_opcion = input("Introduce el número del color (1 para Gris, 2 para Azul o 3 para Amarillo): ").strip()

    if color_opcion == '1':
        color = 'Gris'
    elif color_opcion == '2':
        color = 'Azul'
    elif color_opcion == '3':
        color = 'Amarillo'
    else:
        print("Opción de color no válida para Auto.")
        color = 'Desconocido'

else:
    print("Opción de vehículo no válida.")
    tipo_vehiculo = 'Desconocido'
    color = 'Desconocido'

# Mostrar el resultado final
if tipo_vehiculo == '1':
    print(f"\nHas elegido una Moto de color {color}.")
elif tipo_vehiculo == '2':
    print(f"\nHas elegido un Auto de color {color}.")
else:
    print("\nNo se ha podido procesar tu elección.")