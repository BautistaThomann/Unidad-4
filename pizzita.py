pizza_veg=input("Desea una pizza vegetetariana?\n\t diga si, si desea una pizza veteriana y diga no si no la quiere:").upper()
print ("los ingredientes en todas las pizzas son: tomate y mozzarella.")

if pizza_veg == "SI":
    eleccion=int(input("Los ingredientes vegetarianos son: \n\t 1.tofu \n\t 2.pimiento:\n\t elija un numero: "))

    if eleccion ==1:
     print (" los ingredientes de su pizza son: tofu, tomate y mozzarela ")
    elif eleccion ==2:
     print ("los ingredientes de su pizza son: pimiento, tomate y mozzarela ")
 
if pizza_veg== "NO":
  eleccion2=int(input("Los ingredientes no vegetarianos son: \n\t 3.peperoni \n\t 4.jamon \n\t 5.salmon \n\t elija un numero: "))

  if eleccion2==3:
    print ("los ingredientes de su pizza son: peperoni, tomate y mozzarela")
  elif eleccion2==4:
    print ("los ingredientes de su pizza son: jamon, tomate y mozzarela")
  elif eleccion2==5:
    print ("los ingredientes de su pizza son: salmon,tomate y mozzarela")
