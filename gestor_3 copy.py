from tabulate import tabulate
import csv

curso = []
list_notas = []
otra = "Y"
contador = 1
alumn_nota = None
alumn_nombre = ""


def nuevo_alumno():  # Cambiar formato nombre.
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


with open('3b.csv', 'r') as tercero_b:
    fieldnames = ['ID', 'Nombre', 'Nota', 'Calificacion']
    reader = csv.DictReader(tercero_b, fieldnames=fieldnames)
    for row in reader:
        alumno = row
        curso.append(alumno)

    print(tabulate(curso, headers="keys", tablefmt="fancy_grid"))

option = """Elige una opción:
1. Introducir un nuevo alumno.
2. Modificar un elemento de la tabla.
3. Eliminar un alumno. :"""

pregunta = input("¿Quieres hacer alguna modificación? (Y/N): ").upper()

while pregunta == "Y":

    print(tabulate(curso, headers="keys", tablefmt="fancy_grid"))
    respuesta = int(input(option))

    # Añadir nuevo alumno.
    if respuesta == 1:
        otra = "Y"
        while otra == "Y":
            alumno = nuevo_alumno()

            # Abro mi archivo y guardo los datos del nuevo alumno
            with open('3b.csv', 'a') as tercero_b:
                fieldnames = ['ID', 'Nombre', 'Nota', 'Calificacion']
                writer = csv.DictWriter(tercero_b, fieldnames=fieldnames)
                writer.writerow(alumno)

            # Los datos recogidos se añaden como diccionario a la lista "curso"
            # curso.append(alumno)

            # Bucle para introducir más alumnos en la lista "curso"
            otra = input(
                "¿Quieres introducir otra entrada en el registro? (Y/N): ").upper()

            while otra != "N" and otra != "Y":
                otra = input("Respuesta incorrecta. Introduce Y o N: ").upper()

    if respuesta == 2:
        while True:
            identificador = int(input("Introduce el ID del alumno: "))
            encontrado = False

            for alumno in range(len(curso)):
                if identificador == alumno["ID"]:
                    encontrado = True

                    dato = input(
                        "¿Qué dato quieres modificar: Nombre o Nota: ")

                    if dato == "Nombre":
                        alumn_nombre = input("Introduce un nuevo nombre: ")
                        while not alumn_nombre.isalpha():
                            alumn_nombre = input(
                                "El nombre introducido no es correcto: ")

                        alumno["Nombre"] = alumn_nombre

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

                            alumno["Nota"] = alumn_nota

                            alumno["Calificacion"] = conversion_notas()

                            break

                if encontrado == False:
                    nuevo = str(input(
                        "El ID introducido no corresponde con ningún alumno. ¿Quieres añadir un alumno nuevo? (Y/N): ")).upper()

                    while nuevo == "Y":
                        nuevo_alumno()

            break

    if respuesta == 3:
        identificador = int(input("Introduce el ID del alumno: "))

        encontrado = False
        for alumno in range(len(curso)):
            if curso[alumno]["ID"] == identificador:
                encontrado = True
                del curso[alumno]
                break

    while pregunta != "N" and pregunta != "Y":
        pregunta = input("Respuesta incorrecta. Introduce Y o N: ").upper()

    with open('3b.csv', 'r') as tercero_b:
        reader = csv.DictReader(tercero_b, fieldnames=fieldnames)
        for row in reader:
            alumno = row
            curso.append(alumno)

    print(tabulate(curso, headers="keys", tablefmt="fancy_grid"))

    pregunta = input("¿Quieres hacer otro cambio? (Y/N): ").upper()
    while pregunta != "N" and pregunta != "Y":
        pregunta = input(
            "Respuesta incorrecta. Introduce Y o N: ").upper()
