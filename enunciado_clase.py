calificacion=int(input("ingrese la calificacion del estudiante entre 0 y 100: "))

if calificacion >=90 and calificacion <= 100:
    print ("su calificacion es: A")
elif calificacion  >=80 and  calificacion <=89:
    print("su calificacion es:B")
elif calificacion  >=70 and calificacion <=79:
    print ("su calificacion es: C")
elif calificacion  >=60 and calificacion <=69:
    print ("su calificacion es: D")
elif calificacion >=0 and calificacion <=59:
    print ("su calificacion es: F")