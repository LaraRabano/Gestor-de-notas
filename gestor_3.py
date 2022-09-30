curso = []
contador = 1
list_notas = []
alumn_nombre = ""
alumn_nota = ""


def NuevoAlumno():
    alumn_nombre = input("Introduce un alumno: ")

    while not alumn_nombre.isalpha():
        alumn_nombre = input("El nombre introducido no es correcto: ")

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

    alumno = {
        "ID": contador,
        "Nombre": alumn_nombre,
        "Nota": alumn_nota,
        "Calificacion": ConversionNotas()
    }

    ConversionNotas()
    contador = contador + 1

    # Los datos recogidos se añaden como diccionario a la lista "curso"
    curso.append(alumno)


def ConversionNotas(alumn_nota):

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


print(curso)

option = """Elige una opción:
1. Introducir un nuevo alumno.
2. Modificar un elemento de la tabla.
3. Eliminar un alumno"""

pregunta = input("¿Quieres hacer alguna modificación? (Y/N): ").upper

while pregunta == "Y":
    respuesta = int(input(option))

    # Añadir nuevo alumno.
    if respuesta == 1:
        while otra == "Y":
            NuevoAlumno()

        # Bucle para introducir más alumnos en la lista "curso"
        otra = input(
            "¿Quieres introducir otra entrada en el registro? (Y/N): ").upper()

        while otra != "N" and otra != "Y":
            otra = input("Respuesta incorrecta. Introduce Y o N: ").upper()

    if respuesta == 2:
        while pregunta == "Y":
            identificador = int(input("Introduce el ID del alumno: "))
            encontrado = False

            for alumno in curso:
                if identificador == alumno["ID"]:
                    encontrado = True

                    dato = input(
                        "¿Qué dato quieres modificar: Nombre o Nota: ")

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

                            ConversionNotas()

                            break

            if encontrado == False:
                nuevo = str(input(
                    "El ID introducido no corresponde con ningún alumno. ¿Quieres añadir un alumno nuevo? (Y/N): ")).upper()

                while nuevo == "Y":
                    NuevoAlumno()

        pregunta = input("¿Quieres hacer otro cambio? (Y/N): ").upper()
        while pregunta != "N" and pregunta != "Y":
            pregunta = input(
                "Respuesta incorrecta. Introduce Y o N: ").upper()

    if respuesta == 3:
        identificador = int(input("Introduce el ID del alumno: "))

        encontrado = False
        for alumno in curso:
            if identificador == alumno["ID"]:
                encontrado = True
                del curso[identificador - 1]

    while pregunta != "N" and pregunta != "Y":
        pregunta = input("Respuesta incorrecta. Introduce Y o N: ").upper()
