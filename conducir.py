# Ingresar nombre, apellido y edad, si la edad es igual a 18, muestre un mensaje "solo puede conducir en la ciudad", si es mayor a 18, "usted puede conducir en la colectora", mayor a 21, "libre conduccion" y si es menor a 18, "no puede conducir"

try: 
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))

    if edad == 18:
        print("Solo puede conducir en la cuidad.")
    elif edad > 18 and edad < 21:
        print("Usted puede conducir en la colectora.")
    elif edad >= 21:
        print("Libre condución.")
    elif edad < 18:
        print("No puede conducir.")
    else:
        raise ValueError ("Los datos han sido mal ingresados.")
except ValueError as e:
    print(f"ERROR: {e}")