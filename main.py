from gestor import *

otra = "Y"

while otra == "Y":

    x = introducir_datos()

    otra = input(
                "¿Quieres introducir otra entrada en el registro? (Y/N): ").upper()

            while otra != "N" and otra != "Y":
                otra = input("Respuesta incorrecta. Introduce Y o N: ").upper()