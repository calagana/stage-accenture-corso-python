from collections import defaultdict
from csv import DictReader

from Richiesta import *
from Validator import *
from Pipeline import *

import json

dataset = []

with open("requests.csv", "r") as f:
    reader = DictReader(f)
    for riga in reader:
        dataset.append(riga)


richieste_valide = []
servizi_unici = set()
conteggio_serv = defaultdict(int)

pip = Pipeline()


# Inizio il ciclo per l'analisi
for dict in dataset:

    # Definisco un Validator per dizionario, con le info.
    try:
        val = Validator(dict["id"], dict["nome"], dict["email"], int(dict["eta"]), dict["servizio"])

    except ValueError:
        continue

    #Eseguo i controlli e sanifico i dati
    val.validazione_eta()
    val.validazione_email()
    val.validazione_nome()
    val.sanificazione_dati()

    # Inizio con la pipeline ad aggiungere la categoria eta
    pip.aggiungi_categoria_eta(val)

    # Controllo quindi se la richiesta è valida
    stato_validazione = pip.validazione_richiesta(val)


    # In caso sia valida, aggiungo alla lista
    richieste_valide.append(val.restituisci_dizionario())

    # Creo il dizionario con il conteggio dei servizi
    conteggio_serv[val.restituisci_dizionario()["servizio"]] += 1

    # Aggiungo il servizio al set
    servizi_unici.add(val.restituisci_dizionario()["servizio"])

dizionario_finale = {}

dizionario_finale["totale_richieste"] = len(richieste_valide)
dizionario_finale["servizi_unici"] = list(servizi_unici)      #questo lo converto perchè credo json non supporti i set
dizionario_finale["conteggio_servizi"] = conteggio_serv
dizionario_finale["richiesta"] = richieste_valide

print(dizionario_finale)


with open("output.json", "w") as f:
    json.dump(dizionario_finale, f, indent=4)
