# Ingredientes vegetarianos: pimiento y tofu.
# Ingredientes no vegetarianos: peperoni, Jamón y Salmón.

try:
    pregunta = str(input("¿Quiere una pizza vegetariana? si / no: "))

    if pregunta == "si":
        tipo_de_pizza = str(input("Los ingredientes son los siguientes: \n\t Ingredientes Vegetarianos: pimiento y tofu. \nIngrese los ingredientes que desee (La mozzarella ya esta incluida en todas las pizzas al igual que el tomate) : "))

        if tipo_de_pizza == "pimiento":
            print("Su pizza es vegetariana y tiene los siguientes ingredientes: mozzarella, tomate y pimiento.")
        elif tipo_de_pizza == "tofu":
            print("Su pizza es vegetariana y tiene los siguientes ingredientes: mozzarella, tomate y tofu.")
        else:
            raise ValueError ("No tenemos ese ingrediente, ingrese otra opción")
        
    elif pregunta == "no":
        pregunta2 = str(input("Entonces, ¿Quiere una pizza no vegetariana? si / no: "))
        if pregunta2 == "si":
            tipo_de_pizza = str(input("Ingredientes No Vegetarianos: peperoni, jamon y salmon. \n\tIngrese los ingredientes que desee (La mozzarella ya esta incluida en todas las pizzas al igual que el tomate) : "))
            if tipo_de_pizza == "peperoni":
                print("Su pizza no es vegatariana y tiene los siguientes ingredientes: mozzarella, tomate y peperoni.")
            elif tipo_de_pizza == "jamon":
                print("Su pizza no es vegatariana y tiene los siguientes ingredientes: mozzarella, tomate y jamón.")
            elif tipo_de_pizza == "salmon":
                print("Su pizza no es vegatariana y tiene los siguientes ingredientes: mozzarella, tomate y salmón.")
            else:
                raise ValueError ("No tenemos ese ingrediente, ingrese otra opción")
    else:        
        raise ValueError ("No se han ingresado correctamente los datos.")
except ValueError as e:
    print(f"ERROR: {e}")