print("Bienvenido a la heladeria los 2 gustos")
gustos=int(input("Gustos:\n""1)Chocolate\n""2)Vainilla\n""Respuesta:"))
if gustos==1:
    print ("Gusto elegido chocolate")
    topping=int(input("Seleccione los toppings""\n""1)Almendra\n""2)Caramelo\n""Respuesta:"))
    if topping==1:
        print("Gusto elegido: Chocolate con Almendras")
    elif topping==2:
        print("Gusto elegido: Chocolate con Caramelo")
    else:
        print("1 o 2")

elif gustos==2:
    print ("Gusto elegido Vainilla")
    topping=int(print("Seleccione los toppings""\n""1)Fresas\n""2)Nueces\n""Respuesta:"))
    if topping==1:
        print("Gusto elegido: Vainilla con Fresas")
    elif topping==2:
        print("Gusto elegido: Chocolate con Nueces")
    else:
        print("1 o 2")
else:
    print("1 o 2")