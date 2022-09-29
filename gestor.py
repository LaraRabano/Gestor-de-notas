
"""Soy un profe, y me llega una lista con las notas de mis alumnos de este curso.

Quiero imprimir una lista con el equivalente de cada nota, estas siendo:

Menos de 4 (4 incluido), suspenso; 5 aprobado; 6 bien; 7 y 8 notable; 9 y 10 sobresaliente. (Asume que la lista siempre contiene números del 0 al 10).

Ejemplo:

Entrada: [8, 4, 2, 9, 6, 7, 5, 0]

Salida: [notable, suspenso, suspenso, sobresaliente, bien, notable, aprobado, suspenso]"""

# from tabulate import tabulate

curso = []

otra = "Y"

contador = 1

list_notas = []

alumn_nombre = ""

alumn_nota = ""

# Bucle principal

while otra == "Y":

    # Comprobar que el nombre sólo tiene letras

    alumn_nombre = input("Introduce un alumno: ")
    while not alumn_nombre.isalpha():
        alumn_nombre = input("El nombre introducido no es correcto: ")

    # Comprobar que las notas introducidas son correctas

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

    # Diccionario de cada alumno

    alumn_calificacion = []

    alumno = {
        "ID": contador,
        "Nombre": alumn_nombre,
        "Nota": alumn_nota,
        "Calificacion": ""
    }

    # El contador genera de forma automática el ID de los alumnos por orden de ingreso
    contador = contador + 1

    # Conversión de notas a calificaciones
    if alumn_nota <= 4:
        alumno["Calificacion"] = "Suspenso"

    elif alumn_nota == 5:
        alumno["Calificacion"] = "Aprobado"

    elif alumn_nota == 6:
        alumno["Calificacion"] = "Bien"

    elif alumn_nota == 7 or alumn_nota == 8:
        alumno["Calificacion"] = "Notable"

    elif alumn_nota == 9 or alumn_nota == 10:
        alumno["Calificacion"] = "Sobresaliente"

    # Los datos recogidos se añaden como diccionario a la lista "curso"
    curso.append(alumno)

    # Bucle para introducir más alumnos en la lista "curso"
    otra = input(
        "¿Quieres introducir otra entrada en el registro? (Y/N): ").upper()

    while otra != "N" and otra != "Y":
        otra = input("Respuesta incorrecta. Introduce Y o N: ").upper()

print(curso)
# Impresión de la tabla con los datos de la lista
# print(tabulate(curso, headers="keys", tablefmt="fancy_grid"))

# Fin del bucle principal


# Cambiar elementos de la tabla

pregunta = input(
    "¿Quieres modificar algún elemento de la tabla?(Y/N) ").upper()

while pregunta == "Y":

    identificador = int(input("Introduce el ID del alumno: "))

    #i = id

    encontrado = False
    for alumno in curso:

        if identificador == alumno["ID"]:
            encontrado = True

            # Voy a tener que hacer comprobación de esto.
            dato = input("¿Qué dato quieres modificar: Nombre o Nota: ")

            if dato == "Nombre":
                alumno["Nombre"] = input("Introduce un nuevo nombre: ")
                print(alumno)
                while not alumn_nombre.isalpha():
                    alumn_nombre = input(
                        "El nombre introducido no es correcto: ")

            elif dato == "Nota":
                while True:
                    try:
                        alumn_nota = float(
                            input("Introduce una nueva nota: "))
                        alumno["Nota"] = alumn_nota
                    except:
                        print("La nota introducida no es correcta.")
                        continue

                    if alumn_nota < 0 or alumn_nota > 10:
                        print("La nota introducida no es correcta.")
                        continue

                    # Conversión de notas a calificaciones
                    if alumn_nota <= 4:
                        alumno["Calificacion"] = "Suspenso"

                    elif alumn_nota == 5:
                        alumno["Calificacion"] = "Aprobado"

                    elif alumn_nota == 6:
                        alumno["Calificacion"] = "Bien"

                    elif alumn_nota == 7 or alumn_nota == 8:
                        alumno["Calificacion"] = "Notable"

                    elif alumn_nota == 9 or alumn_nota == 10:
                        alumno["Calificacion"] = "Sobresaliente"

                    break

    if encontrado == False:
        nuevo = str(input(
            "El ID introducido no corresponde con ningún alumno. ¿Quieres añadir un alumno nuevo? (Y/N): ")).upper()

        while nuevo == "Y":
            # Comprobar que el nombre sólo tiene letras

            alumn_nombre = input("Introduce un alumno: ")
            while not alumn_nombre.isalpha():
                alumn_nombre = input(
                    "El nombre introducido no es correcto: ")

            # Comprobar que las notas introducidas son correctas

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

            # Diccionario de cada alumno

            alumn_calificacion = []

            alumno = {
                "ID": contador,
                "Nombre": alumn_nombre,
                "Nota": alumn_nota,
                "Calificacion": ""
            }

            # El contador genera de forma automática el ID de los alumnos por orden de ingreso
            contador = contador + 1

            # Conversión de notas a calificaciones
            if alumn_nota <= 4:
                alumno["Calificacion"] = "Suspenso"

            elif alumn_nota == 5:
                alumno["Calificacion"] = "Aprobado"

            elif alumn_nota == 6:
                alumno["Calificacion"] = "Bien"

            elif alumn_nota == 7 or alumn_nota == 8:
                alumno["Calificacion"] = "Notable"

            elif alumn_nota == 9 or alumn_nota == 10:
                alumno["Calificacion"] = "Sobresaliente"

            # Los datos recogidos se añaden como diccionario a la lista "curso"
            curso.append(alumno)

            print(curso)
            # Impresión de la tabla con los datos de la lista
            # print(tabulate(curso, headers="keys", tablefmt="fancy_grid"))

    pregunta = input("¿Quieres hacer otro cambio? (Y/N): ").upper()
    while pregunta != "N" and pregunta != "Y":
        pregunta = input(
            "Respuesta incorrecta. Introduce Y o N: ").upper()

print(curso)


eliminar = input(
    "¿Quieres eliminar algún elemento de la tabla?(Y/N) ").upper()

if eliminar == "Y":

    identificador = int(input("Introduce el ID del alumno: "))

    encontrado = False
    for alumno in curso:
        if identificador == alumno["ID"]:
            encontrado = True
            del curso[identificador - 1]


print(curso)
