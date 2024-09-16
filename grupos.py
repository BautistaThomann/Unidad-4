try:
    nombre = input("Ingrese su nombre: ").capitalize()
    sexo = input("Ingrese su sexo (hombre/mujer): ")
    
    primera_letra = nombre.upper()
    
    if sexo == "hombre":
        if primera_letra > "N":
            grupo = "Grupo A"
        else:
            grupo = "Grupo B"
    elif sexo == "mujer":
        if nombre < "M":
            grupo = "Grupo A"
        else:
            grupo = "Grupo B"
    else:
        raise ValueError ("Sexo no valido, ingrese *hombre o mujer*.")
    print(f"Usted pertenese al {grupo}.")
except ValueError as e:
    print(f"ERROR: {e}")