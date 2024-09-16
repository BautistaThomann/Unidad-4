#Ingredientes vegetarianos : pimiento y tofu 
#Ingredientes no vegetarianos : peperoni, jamon y salmon

try: 
    pregunta= str(input("¿Quiere una pizza vegetariana? si/no: "))

    if pregunta == "si":
        tipo_de_pizza = str(input("Los ingredientes son los siguientes: \n\t Ingredientes Vegetarianos : pimiento y tofu. \nIngrese los ingredientes que desee (la mozzarella y el tomate van incluidos ya en su pizza.) : "))

        if tipo_de_pizza == "pimiento":
            print("Su pizza es vegetariana y tiene los siguientes ingredientes : mozzarella, tomate y pimiento.")
        elif tipo_de_pizza == "tofu":
            print("Su pizza es vegetariana y tiene los siguientes ingredientes : mozzarella, tomate y tofu. ")
        else: 
            raise ValueError ("No tenemos ese ingrediente, ingrese otra opcion.")
        
    elif pregunta == "no":
        pregunta2 = str(input("Entonces, ¿Quiere una pizza no vegetariana? si / no: "))
        if pregunta2 == "si":
            tipo_de_pizza = str(input("Ingredientes no vegetarianos: peperoni; jamon y salmon. \n\tIngrese los ingredientes que desee (la mozzarella y el tomate van incluidos ya en su pizza.) :  "))
            if tipo_de_pizza == "peperoni":
                print("Su pizza no es vegetariana y tiene los siguientes ingredientes : mozzarella, tomate y peperoni:")
            elif tipo_de_pizza == "jamon":
                print("Su pizza no es vegetariana y tiene los siguientes ingredientes : mozzarella, tomate y jamon:")
            elif tipo_de_pizza == "salmon":
                print("Su pizza no es vegetariana y tiene los siguientes ingredientes : mozzarella, tomate y salmon:")
            else: 
                raise ValueError ("No tenemos ese ingrediente, ingrese otra opcion.")
    else: 
        raise ValueError ("No se han ingresado correctamente los datos.")
except ValueError as e:
    print(f"ERROR: {e}")













































