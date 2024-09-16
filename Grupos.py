def buscar_grupo_sexo():
    sexo = str(input("Ingrese su sexo: "))
    sexo_mayuscula = sexo.upper()
    primer_letra_sexo = sexo_mayuscula[0]
    if primer_letra_sexo > 'F':
        buscar_grupo_masculino()
    else:
        buscar_grupo()

def buscar_grupo_masculino():
    nombre = str(input("Ingrese su nombre: "))
    nombre_mayusculas = nombre.upper()
    primer_letra = nombre_mayusculas[0]
    if 'N' <=  primer_letra <= 'Z':
        grupo = 'A'
    else:
        grupo = 'B'
    print(grupo)


def buscar_grupo():
    nombre = str(input("Ingrese su nombre: "))
    nombre_mayusculas = nombre.upper()
    primer_letra = nombre_mayusculas[0]
    if 'A' <=  primer_letra <= 'M':
        grupo = 'A'
    else:
        grupo = 'B'
    print(grupo)

buscar_grupo_sexo()
