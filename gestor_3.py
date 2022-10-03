
curso = []
list_notas = []
otra = "Y"
contador = 0

def nuevo_alumno(): #Cambiar formato nombre.
    global contador
    alumn_nombre = IntroducirNombre()
    alumn_nota = IntroducirNota()
    alumn_calificacion = ConversionNotas()
    
    alumno = {
        "ID": contador,
        "Nombre": alumn_nombre,
        "Nota": alumn_nota,
        "Calificacion": alumn_calificacion
    }

    contador = contador + 1
    return alumno


def IntroducirNombre():
    alumn_nombre = input("Introduce un alumno: ")

    while not alumn_nombre.isalpha():
        alumn_nombre = input("El nombre introducido no es correcto: ")

    return alumn_nombre


def IntroducirNota():
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


def ConversionNotas():

    alumn_calificacion = ""

    nota = IntroducirNota()

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


print(curso)

option = """Elige una opción:
1. Introducir un nuevo alumno.
2. Modificar un elemento de la tabla.
3. Eliminar un alumno. :"""

pregunta = input("¿Quieres hacer alguna modificación? (Y/N): ").upper()

while pregunta == "Y":
    respuesta = int(input(option))

    # Añadir nuevo alumno.
    if respuesta == 1:
        while otra == "Y":
            alumno = NuevoAlumno()

            # Los datos recogidos se añaden como diccionario a la lista "curso"
            curso.append(alumno)

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
