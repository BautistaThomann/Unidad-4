vehiculos=int(input("Bienvenido, seleccione uno de los vehiculos disponibles: \n1. Moto \n2. Auto\nElija una opcion:"))
if vehiculos == 1:
    print ("Los colores disponibles del vehiculo son rojo, blanco y negro")
    color1=int(input("elija un color: \n1. Rojo \n2. Blanco \n3. Negro\nElija una opcion:1"))
    if color1 == 1:
        print("El vehiculo seleccionado es una moto de color rojo")
    elif color1 == 2:
            print("El vehiculo seleccionado es una moto de color blanco")
    else:
        print("El vehiculo seleccionado es una moto de color negro")        
else:
    print("Los colores disponibles del vehiculos son: gris, azul y amarillo")
    color2=int(input("Elija un color: \n1.  Gris \n2. Azul \n3. Amarillo\nElija una opcion:"))
    if color2 == 1:
      print("El vehiculo seleccionado es un auto de color gris")
    elif color2 == 2:
        print("El vehiculo seleccionado es un auto de color azul") 
    else:
        print("El vehiculo seleccionado es un auto de color amarillo")    
     


 


