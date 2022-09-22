"""Soy un profe, y me llega una lista con las notas de mis alumnos de este curso.

Quiero imprimir una lista con el equivalente de cada nota, estas siendo:

Menos de 4 (4 incluido), suspenso; 5 aprobado; 6 bien; 7 y 8 notable; 9 y 10 sobresaliente. (Asume que la lista siempre contiene números del 0 al 10).

Ejemplo:

Entrada: [8, 4, 2, 9, 6, 7, 5, 0]

Salida: [notable, suspenso, suspenso, sobresaliente, bien, notable, aprobado, suspenso]"""


notas = []  

otra = "Y"

while otra == "Y":

    try:
        notas.append(int(input("Introduce una nota: ")))

    except ValueError:
        print("El número introducido no es correcto")
        continue

    otra = input("¿Quieres introducir otra nota? (Y/N): ").upper()
    

    while otra != "N" and otra != "Y":
        otra = input("Respuesta incorrecta. Introduce Y o N: ").upper()
    

            


 
lista_notas = []

for i in notas:

    if i <= 4:
        lista_notas.append("Suspenso")
    
    elif i == 5:
        lista_notas.append("Aprobado")

    elif i == 6:
        lista_notas.append("Bien")
    
    elif i == 7 or i == 8:
        lista_notas.append("Notable")

    elif i == 9 or i == 10:
        lista_notas.append("Sobresaliente")

print(lista_notas)



    

    