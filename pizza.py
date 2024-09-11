# Ingredientes vegetarianos: pimiento y tofu.
# Ingredientes no vegetarianos: peperoni, Jamón y Salmón.

pregunta = str(input("¿Quiere una pizza vegetariana? : "))

if pregunta == "si":
    tipo_de_pizza = str(input("Los ingredientes son los siguientes: \n\t Ingredientes Vegetarianos: pimiento y tofu. \n\t Ingredientes No Vegetarianos: peperoni, jamon y salmon. \n Ingrese los ingredientes que desee (La mozzarella ya esta incluida en todas las pizzas al igual que el tomate): "))

    if tipo_de_pizza == "pimiento":
        print("Su pizza es vegetariana y tiene los siguientes ingredientes: mozzarella, tomate y pimiento.")
    elif tipo_de_pizza == "tofu":
        print("Su pizza es vegetariana y tiene los siguientes ingredientes: mozzarella, tomate y tofu.")
    elif tipo_de_pizza == "peperoni":
        print("Su pizza no es vegatariana y tiene los siguientes ingredientes: mozzarella, tomate y peperoni.")
    elif tipo_de_pizza == "jamon":
        print("Su pizza no es vegatariana y tiene los siguientes ingredientes: mozzarella, tomate y jamon.")
    elif tipo_de_pizza == "salmon":
        print("Su pizza no es vegatariana y tiene los siguientes ingredientes: mozzarella, tomate y salmon.")
    else:
        print("Lo sentimos, no tenemos ese ingrediente.")
else:
    print("Bueno esta bien, no hay drama.")