def obtener_datos():
    while True:
        try:
            nombre_apellido = input('Ingrese su nombre y apellido: ').strip()
            edad = int(input('Ingrese su edad: '))
            if edad < 0:
                print("La edad no puede ser negativa. Por favor ingresa una edad válida.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número entero para la edad.")
    
    if edad < 18:
        print('Usted no puede conducir')
    elif edad == 18:
        print('Solo puede conducir en la ciudad')
    elif edad > 21:
        print('Libre conducción')
    else:
        print('Usted puede conducir en la colectora')

obtener_datos()
