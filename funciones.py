def nuevo_alumno():  # TODO Cambiar formato nombre.
    global contador
    global alumn_nota
    global alumn_nombre
    alumn_nombre = introducir_nombre()
    alumn_nota = introducir_nota()
    alumn_calificacion = conversion_notas()

    alumno = {
        "ID": contador,
        "Nombre": alumn_nombre,
        "Nota": alumn_nota,
        "Calificacion": alumn_calificacion
    }

    contador = contador + 1
    return alumno


def introducir_nombre():
    global alumn_nombre
    alumn_nombre = input("Introduce un alumno: ")

    while not alumn_nombre.isalpha():
        alumn_nombre = input("El nombre introducido no es correcto: ")

    return alumn_nombre


def introducir_nota():
    while True:
        try:
            alumn_nota = float(input("Introduce una nota: "))
        except:
            print("La nota introducida no es correcta.")
            continue
        if alumn_nota < 0 or alumn_nota > 10:
            print("La nota introducida no es correcta.")
            continue
        break

    return alumn_nota


def conversion_notas():

    alumn_calificacion = ""

    nota = alumn_nota

    if nota <= 4:
        alumn_calificacion = "Suspenso"

    elif nota == 5:
        alumn_calificacion = "Aprobado"

    elif nota == 6:
        alumn_calificacion = "Bien"

    elif nota == 7 or nota == 8:
        alumn_calificacion = "Notable"

    elif nota == 9 or nota == 10:
        alumn_calificacion = "Sobresaliente"

    return alumn_calificacion