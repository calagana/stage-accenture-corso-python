import csv

with open("dati_prodotti.csv", "w", newline="") as f:

    fieldnames = ["id","nome","prezzo"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({"id":1,"nome":"PC","prezzo":999})
    writer.writerow({"id": 2, "nome": "Monitor", "prezzo": 699})
    writer.writerow({"id": 3, "nome": "Mouse", "prezzo": 99})
    writer.writerow({"id": 4, "nome": "Tastiera", "prezzo": 129})