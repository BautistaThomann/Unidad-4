#Crea un pequeño juego donde narres una historia, “estilo elige tu propia aventura”, con un principio, 
# dos o mas caminos a seguir, y uno o varios finales del juego.
def historia():
    print('Estas en un bosque y te encontras con una cueva tenebrosa.\n1)Entras\n2)Seguis caminando por el bosque')
    eleccion1 = int(input('Escoge tu opcion 1-2: '))
    if eleccion1 == 1:
        dentro_cueva()
    else:
        afuera_cueva()
            
def dentro_cueva():
    print('Encuentras una antorcha con un encendedor. \n 1)La enciendes\n2)Sigues a oscuras')
    antorcha_eleccion = int(input('Escoge tu opcion 1-2:'))
    if antorcha_eleccion == 1:
        print('Felicidades, gracias a la luz del fuego te encontraste en el piso una espada tirada.\nPudiste defenderte de los mounstruos. Lograste salir de la cueva sano y salvo.')
    else:
        print('Tus instintos te fallaron. Te atacaron los mounstruos.\nPerdiste.')

def afuera_cueva():
    print('De repente te encontras un rio con una fuerte corriente y vez una soga colgando de un arbol a la mitad del rio.\n1)Cruzas con la soga\n2)Cruzas nadando ')
    rio_eleccion = int(input('Escoge una opcion 1-2:'))
    if rio_eleccion == 1:
        print('Felicidades llegaste a tu destino sano y salvo.')
    else:
        print('Fuiste mas debil que la corriente. Perdiste.')
historia()
 
