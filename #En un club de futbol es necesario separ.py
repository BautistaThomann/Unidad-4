#En un club de futbol es necesario separar a los chicos por categoria para poder empezar a entrenarlos. Los chicos mayores de 5 años estaran en la categoria A, Los chicos mayores de 10 años y menores de 12 estaran en la categoria B y los niños mayores de 12 años y menores de 16 estaran en la categoria C 

#Se necesita elaborar un programa para facilitar el separar por categoria a los chicos  

#El programa debe preguntar el nombre de los niños, edad y separarlos por categoria  
nombre=str(input("Ingrese el nombre del niño: "))
edad = int(input("Ingrese la edad: "))
if (5<=edad<10):
    categoria='A'
    print (f"{nombre} categoria: {categoria}")
elif 10<edad>=12:
    categoria='B'
    print (f"{nombre} categoria: {categoria}")
elif(edad>12):
    categoria='C'
    print (f"{nombre} categoria: {categoria}")
else: print("Error")
   