try:
    
    edad = int(input("Ingrese su edad antes de ingresar al boliche: "))
    if edad >= 18:
        print("¡¡Bienvenido!!")
    elif edad < 18:
        print("Sos menor de edad, no puede ingresar.")
        exit()
    else:
        raise ValueError ("No se ingresaron correctamente los datos.")
    
    de_donde_viene = str(input("¿Venis de otro pueblo o ciudad? si / no: "))

    if de_donde_viene == "si":
        print("Tenes entrada gratuita y una consumición gratis.")
        if edad >= 20:
            ingreso_vip = str(input("Usted puede ingresar al VIP, ¿Desea ingresar? si / no : "))
            if ingreso_vip == "si":
                print("¡Bienvenido al VIP!")
            elif ingreso_vip == "no":
                print("No se preocupe, ¡Disfrute del boliche!")
            else:
                raise ValueError ("No se ingresaron correctamente los datos.")
    elif de_donde_viene == "no":
        print("¡Disfrute del boliche!")
        if edad >= 20:
            ingreso_vip = str(input("Usted puede ingresar al VIP, ¿Desea ingresar? si / no : "))
            if ingreso_vip == "si":
                print("¡Bienvenido al VIP!")
            elif ingreso_vip == "no":
                print("No se preocupe, ¡Disfrute del boliche!")
            else:
                raise ValueError ("No se ingresaron correctamente los datos.")
    else:
        raise ValueError ("No se ingresaron correctamente los datos.")
except ValueError as e:
    print(f"ERROR: {e}")