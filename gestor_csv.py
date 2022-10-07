from tabulate import tabulate
import csv
from funciones import *


curso = []
list_notas = []
otra = "Y"
contador = 1
alumn_nota = None
alumn_nombre = ""

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
