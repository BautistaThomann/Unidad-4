try: 
    pregunta = str(input("Desea una pizza vegetariana?: "))
    
    if pregunta == "si":
        elegir_pizza = str(input("Los ingredientes de la pizza vegetariana son: \n Pizza vegetariana: Pimiento y Tofu.\n 'La Mozzarella y el Tomate estan incluidos en todas las pizzas' \n Ingrese los ingredientes deseados: "))
            
        if elegir_pizza == "Pimiento":   
            print("Su pizza es vegetariana y tiene los siguientes ingredientes: Mozzarella, Tomate y Pimiento.")
        elif elegir_pizza == "Tofu":
            print("Su pizza es vegetariana y tiene los siguientes ingredientes: Mozarella, Tomate y Tofu.")
        else: 
            raise ValueError ("No tenemos ese ingrediente, ingrese otra opcion")    
    else:         
        pregunta = str(input("Entonces desea una pizza no vegetariana?: "))        
        if pregunta == "si":
            elegir_pizza = str(input("Los ingredientes de la pizza no vegetariana son: Peperoni, Jamon y Salmon \n'La muzzarella y el Tomate estan incluidos en todas las pizzas.\nIngrese el ingrediente deseado: "))
            if elegir_pizza == elegir_pizza == "Peperoni": 
                print("Su pizza no es vegetariana y tiene los siguientes ingredientes: Mozzarella, Tomate y Peperoni.")            
            elif elegir_pizza == "Jamon":
                print("Su pizza no es vegetariana y tiene los siguientes ingredientes: Mozzarella, Tomate y Jamon.")
            elif elegir_pizza == "Salmon":
                print("Su pizza no es vegetariana y tiene los siguientes ingredientes: Mozarella, Tomate y Salmon.")
            else: 
                raise ValueError ("No tenemos ese ingrediente, ingrese otra opcion")
        else:
            raise ValueError ("No se han ingresado los datos correctamente.")    
except ValueError as e:
    print (f"ERROR: {e}")                
