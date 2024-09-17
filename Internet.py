nombre=str(input("Ingrese su nombre:"))
apellido=str(input("Ingrese su apellido:"))
opcion=int(input("Ingrese una opción:\n1- 30 megas\n2- 50 megas\n3- 100 megas\n"))
if opcion==1:
    monto=750-0.10*750
    print(f"{nombre}{apellido} Monto a pagar:{monto}")
elif(opcion==2):
    print(f"{nombre}{apellido} Monto a pagar:{930-0.5*930}")
elif(opcion==3):
    print(f"Cliente: {nombre}{apellido} Monto a pagar:{930-0.5*930}")
else: print("Opción inválida")