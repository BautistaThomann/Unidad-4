def veg_siono ():
    tipo_de_pizza = str(input("Ingrese el tipo de pizza que desea (Vegetariana o no): "))
    pizza_mayus = tipo_de_pizza.upper()
    pizza_distinguir = pizza_mayus[0]
    if pizza_distinguir >= 'V':
        vegetariana ()
    else: 
        novegetariana ()

def vegetariana ():
    #PIMIENTO Y TOFU
    print('Las opciones de ingredientes son: \n1) PIMIENTO \n2) TOFU\n')
    opcion_valida1 = {'1'}
    opcion_valida2 = {'2'}
    while True:
        entrada = input("Por favor, escoja una opcion: ")
        if entrada in opcion_valida1:
            print("Su pedido de una pizza VEGETARIANA con MOZZARELLA, TOMATE Y PIMIENTO ha sido realizado con exito. Muchas gracias.")
            return veg_siono
        else:
            print("Su pedido de una pizza VEGETARIANA con MOZZARELLA, TOMATE Y TOFU ha sido realizado con exito. Muchas gracias.")
            return veg_siono

def novegetariana():
    #PEPERONI, JAMON Y SALMON
    print ('Las opciones de ingredientes son: \n1)PEPERONI\n2)JAMON\n3)SALMON')
    opcion1 = {'1'}
    opcion2 = {'2'}
    opcion3 = {'3'}
    while True:
        eleccion = input('Por favor, escoja una opcion: ')
        if eleccion in opcion1:
            print('Su pedido de una pizza NO VEGETARIANA con MOZZARELLA, TOMATE Y PEPERONI ha sido realizado con exito. Muchas gracias.')
            return veg_siono
        if eleccion in opcion2:
            print('Su pedido de una pizza NO VEGETARIANA con MOZZARELLA, TOMATE Y JAMON ha sido realizado con exito. Muchas gracias.')
            return veg_siono
        if eleccion in opcion3:
            print('Su pedido de una pizza NO VEGETARIANA con MOZZARELLA, TOMATE Y SALMON ha sido realizado con exito. Muchas gracias.')
            return veg_siono
veg_siono()
        

           
        
            

    
    