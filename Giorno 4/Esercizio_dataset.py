import csv
import json


utenti = []

with open("esercizio_dataset_csv_json.txt", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        utenti.append(row)


#Adesso sanifichiamo i dati - trovo gli utenti validi

utenti_validi = []
utenti_non_validi = []

for dict in utenti:
#    print(dict)
    validita = True

    #Devo vedere se la flag dell'età funziona:
    try:
        eta = int(dict["eta"])
    except ValueError:
        validita = False
    else:
        for k in dict:
            if dict[k] == "":
                validita = False
                break


    #infine controllo che il nome con

    if validita:
        utenti_validi.append(dict)
    else:
        utenti_non_validi.append(dict)

#Qui ho quindi gli utenti validi e non validi. Non rimane che pulirli e stamparli (pulisco solo quelli validi)
#Aggiungo anche la flag della seniority

for dict in utenti_validi:
    dict["nome"] = dict["nome"].strip().title()
    dict["citta"] = dict["citta"].strip().title()

    try:
        if int(dict["eta"]) >= 30:
            dict["Seniority"] = "Senior"
        elif int(dict["eta"]) > 25:
            dict["Seniority"] = "Mid"
        elif int(dict["eta"]) > 18:
            dict["Seniority"] = "Junior"
        else:
            dict["Seniority"] = "NV"
    except ValueError:
        print(f"")

#Non rimane che stampare il cvs e stampare il json

with open("utenti_validi.json", "w") as f_out:
    json.dump(utenti_validi, f_out, indent = 4)

#Inoltre stampo anche il csv

with open("utenti_validi.csv", "w", newline = "") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=["nome","eta","citta","Seniority"])
    writer.writeheader()
    writer.writerows(utenti_validi)

with open("utenti_non_validi.csv", "w", newline = "") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=["nome","eta","citta","Seniority"])
    writer.writeheader()
    writer.writerows(utenti_non_validi)