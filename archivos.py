"""questions = open("questions.txt", "r")


texto = questions.readlines()

for i in texto:
    print(i[:-1])"""

total = []
resultados = []
respuesta_correcta = []
with open('questions.txt', 'r+') as questions:
    for linea in questions.readlines():
        igual = linea.find("=")+1
        respuesta = input(linea[:igual])
        total.append(respuesta)
    print(f"Tus respuestas son {total}")
    questions.seek(0)

# with open('questions.txt', 'r+') as questions:
    for linea in questions.readlines():
        igual = linea.find("=")+1
        respuesta_correcta.append(linea[igual:-1])

    for r, c in zip(total, respuesta_correcta):
        if r == c:
            resultados.append("Correcto")
        else:
            resultados.append(f"La respuesta correcta es {c}")

    print(resultados)
