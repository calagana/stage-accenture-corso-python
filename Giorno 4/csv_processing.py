import csv
with open("dati.csv", newline="") as f:  #newline indica quando nel csv c'è una nuova riga
    reader = csv.reader(f)

    for riga in reader:
        print(riga)

dataset = []

with open("dati.csv", newline="") as f:  #newline indica quando nel csv c'è una nuova riga
    reader = csv.DictReader(f)      #Così crea direttamente un dizionario!

    for riga in reader:
        dataset.append(riga)

print(dataset)

#Per scrivere invece
with open("dati.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["nome","eta","Citta"])