print("Bienvenido a Elian")
ciudad=int(input("Ciudad de origen:\n""1)Villa Maria\n""2)Otros\n""Respuesta:"))
if ciudad==1:
    print("Cobrar entrada")
elif ciudad==2:
    print("Entrada libre y gratuita")    
edad=int(input("Ingrese su edad\n""Respuesta:"))
if edad<18:
    print("No puede ingresar")
elif edad>18 and edad<20:
    print("Entrada comun")
else:
    print("Entrada comun + acceso al vip")
    pregunta=int(input("Quiere ingresar al vip?\n""1)Si\n""2)No\n""Respuesta:"))
    if pregunta==1:
        print("Bienvenido a Elian VIp!")
    elif pregunta==2:
        print("Bienvenido a Elian!")            