
import csv
curso = []

alumno = {
    "ID": "2",
    "Nombre": "Bea",
    "Nota": "8",
    "Calificacion": "Notable"
}


with open('3b.csv', 'a') as tercero_b:
    fieldnames = ['ID', 'Nombre', 'Nota', 'Calificacion']
    writer = csv.DictWriter(tercero_b, fieldnames=fieldnames)
    writer.writerow(alumno)


with open('3b.csv', 'r') as tercero_b:
    reader = csv.DictReader(tercero_b, fieldnames=fieldnames)
    for row in reader:
        alumno = row
        curso.append(alumno)


print(curso)
