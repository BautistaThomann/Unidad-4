nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
tipo_serv=int(input("ingrese el tipo de servicio que tiene 1, 2 o 3: "))
tipo_serv1=750-(750*0.10)
tipo_serv2=930-(930*0.05)
tipo_serv3=1200
if tipo_serv==1:
    print (f"El cliente {nombre} {apellido}, debe abonar un total de: {tipo_serv1}")
elif tipo_serv==2:
    print(f"El cliente {nombre} {apellido}, debe abonar un total de: {tipo_serv2}")
elif tipo_serv==3:
    print(f"El cliente {nombre} {apellido}, debe abonar un total de: {tipo_serv3}")
