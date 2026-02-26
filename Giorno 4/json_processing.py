import json

with open("utente.json", "r") as f:
    dati = json.load(f)

print(dati)    #Python l'ha resa un dict praticamente!!!
print(dati["nome"])

utente = {
    "nome": "Anna",
    "eta" : 22
}

with open("utente.json", "w") as f:
    json.dump(utente, f, indent = 4) #indent mette gli spazi

with open("utenti.json", "r") as f_in:
    utenti = json.load(f_in)

print(type(utenti))   #è proprio una lista!

for u in utenti:
    eta = u["eta"]
    print(type(eta))
    if eta>27:
        u["categoria"] = "Senior"
    else:
        u["categoria"] = "Junior"

print(utenti)
with open("utenti_classificati.json", "w") as f_out:
    json.dump(utenti, f_out, indent = 4)