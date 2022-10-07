
"""Soy un profe, y me llega una lista con las notas de mis alumnos de este curso.

Quiero imprimir una lista con el equivalente de cada nota, estas siendo:

Menos de 4 (4 incluido), suspenso; 5 aprobado; 6 bien; 7 y 8 notable; 9 y 10 sobresaliente. (Asume que la lista siempre contiene números del 0 al 10).

Ejemplo:

Entrada: [8, 4, 2, 9, 6, 7, 5, 0]

Salida: [notable, suspenso, suspenso, sobresaliente, bien, notable, aprobado, suspenso]"""


from tabulate import tabulate


class Curso:

    def __init__(self):

        self.curso = []

        self.otra = "Y"

        self.alumno = {"ID": None,
                       "Nombre": None,
                       "Nota": None,
                       "Calificación": None}

        pass

    def introducir_datos(self):

        self.alumno = {"ID": int(input("Introduce el identificador del alumno: ")),
                       "Nombre": str(input("Introduce un alumno: ")),
                       "Nota": int(input("Introduce una nota: ")),
                       "Calificación": calcular_nota()}

        self.curso.append(self.alumno)

        otra = input(
            "¿Quieres introducir otra entrada en el registro? (Y/N): ").upper()

        while otra != "N" and otra != "Y":
            otra = input("Respuesta incorrecta. Introduce Y o N: ").upper()

    def calcular_nota(self):

        for nota in self.alumno:

            if nota <= 4:
                nota: "Suspenso"

            elif nota == 5:
                nota: "Aprobado"

            elif nota == 6:
                nota: "Bien"

            elif nota == 7 or nota == 8:
                nota: "Notable"

            elif nota == 9 or nota == 10:
                nota: "Sobresaliente"


print(tabulate(self.curso, headers=["Identificador",
      "Nombre", "Nota", "Calificación"]))


pregunta = input("¿Quieres modificar algún elemento de la tabla?(Y/N ")

while pregunta == "Y":

    """Planteamiento para buscar los datos que queremos modificar"""

    while pregunta != "N" and pregunta != "Y":
        pregunta = input("Respuesta incorrecta. Introduce Y o N: ").upper()
