
"""Soy un profe, y me llega una lista con las notas de mis alumnos de este curso.

Quiero imprimir una lista con el equivalente de cada nota, estas siendo:

Menos de 4 (4 incluido), suspenso; 5 aprobado; 6 bien; 7 y 8 notable; 9 y 10 sobresaliente. (Asume que la lista siempre contiene números del 0 al 10).

Ejemplo:

Entrada: [8, 4, 2, 9, 6, 7, 5, 0]

Salida: [notable, suspenso, suspenso, sobresaliente, bien, notable, aprobado, suspenso]"""


import json


curso = []

otra = "Y"

alumno = {"ID": None,
          "Nombre": None,
          "Nota": None,
          "Calificacion": None}


while otra == "Y":

    list_notas = []

    alumno = {"ID": int(input("Introduce el identificador del alumno: ")),
              "Nombre": str(input("Introduce un alumno: ")),
              "Nota": int(input("Introduce una nota: ")),
              "Calificacion": list_notas}

    if alumno.get("Nota") <= 4:
        list_notas.append("Suspenso")

    elif alumno.get("Nota") == 5:
        list_notas.append("Aprobado")

    elif alumno.get("Nota") == 6:
        list_notas.append("Bien")

    elif alumno.get("Nota") == 7 or alumno.get("Nota") == 8:
        list_notas.append("Notable")

    elif alumno.get("Nota") == 9 or alumno.get("Nota") == 10:
        list_notas.append("Sobresaliente")

    curso.append(alumno)

    otra = input(
        "¿Quieres introducir otra entrada en el registro? (Y/N): ").upper()

    while otra != "N" and otra != "Y":
        otra = input("Respuesta incorrecta. Introduce Y o N: ").upper()

print(json.dumps(curso, indent=2))


"""pregunta = input("¿Quieres modificar algún elemento de la tabla?(Y/N ")

while pregunta == "Y":

    Planteamiento para buscar los datos que queremos modificar

    while pregunta != "N" and pregunta != "Y":
        pregunta = input("Respuesta incorrecta. Introduce Y o N: ").upper()"""
