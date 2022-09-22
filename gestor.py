"""Soy un profe, y me llega una lista con las notas de mis alumnos de este curso.

Quiero imprimir una lista con el equivalente de cada nota, estas siendo:

Menos de 4 (4 incluido), suspenso; 5 aprobado; 6 bien; 7 y 8 notable; 9 y 10 sobresaliente. (Asume que la lista siempre contiene números del 0 al 10).

Ejemplo:

Entrada: [8, 4, 2, 9, 6, 7, 5, 0]

Salida: [notable, suspenso, suspenso, sobresaliente, bien, notable, aprobado, suspenso]"""


from tabulate import tabulate


curso = [id_alumno := [], alumno := [], nota := [], calificación := []]

otra = "Y"


while otra == "Y":

    id_alumno.append(int(input("Introduce el identificador del alumno: ")))

    alumno.append(str(input("Introduce un alumno: ")))

    nota.append(int(input("Introduce una nota: ")))

    otra = input(
        "¿Quieres introducir otra entrada en el registro? (Y/N): ").upper()

    while otra != "N" and otra != "Y":
        otra = input("Respuesta incorrecta. Introduce Y o N: ").upper()


for i in nota:

    if i <= 4:
        calificación.append("Suspenso")

    elif i == 5:
        calificación.append("Aprobado")

    elif i == 6:
        calificación.append("Bien")

    elif i == 7 or nota == 8:
        calificación.append("Notable")

    elif i == 9 or nota == 10:
        calificación.append("Sobresaliente")


print(tabulate(curso, headers=["Identificador",
      "Nombre", "Nota", "Calificación"]))


pregunta = input("¿Quieres modificar algún elemento de la tabla?(Y/N ")

while pregunta == "Y":

    """Planteamiento para buscar los datos que queremos modificar"""

    while pregunta != "N" and pregunta != "Y":
        pregunta = input("Respuesta incorrecta. Introduce Y o N: ").upper()
