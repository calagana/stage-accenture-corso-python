#with open("dati.txt", "a") as f:
#    f.write("\nSono contenuto nuovo")


with open("dati.txt", "r") as f:
    nomi = f.readlines()

nomi_puliti = []
for n in nomi:
    nome = n.strip()
    nome = nome.title()
    nome = nome.replace("\n","")
    nomi_puliti.append(nome)

print(nomi_puliti)

#Creo un altro file dove scrivere i nomi puliti

with open("dati_puliti.txt", "w") as f:
    for nome in nomi_puliti:
        f.write(nome+"\n")


#E con una comprehension? Non lo runno ma questo è il modulo. Anche .join si può usare
with open("dati.txt", "r") as f:
    nomi_puliti_c = [r.strip().title().replace("\n","") for r in f.readlines()]