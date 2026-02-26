#Aggiungere una colonna "categoria"
#Se l'età >=27 , la categoria è senior, altrimenti junior

import csv

dizionario_dati = []
filenames = []
with open("esercizio.csv", "r") as f:
    reader = csv.DictReader(f)
    filenames = reader.fieldnames
    for row in reader:
        dizionario_dati.append(row)

filenames.append("categoria")
for dizionario in dizionario_dati:
    if int(dizionario["eta"]) >= 27:
        dizionario["categoria"] = "Senior"
    else:
        dizionario["categoria"] = "Junior"


with open("esercizio.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=filenames)
    writer.writeheader()

    for dizionario in dizionario_dati:
        writer.writerow(dizionario)