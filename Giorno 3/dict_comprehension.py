numeri = [3,6,9,12,15,18,21,24,27,30]

#crea dizionario chiave-> numero ,, valore ->numero/3

divisi = {n: n/3 for n in numeri}
print(divisi)


#Es 2: nomi. Crea dizionario chiave->nome, valore->"lungo se lunghezza è >5, altrimenti "corto"
nomi = ["Anna", "Ciccio", "Francesca", "Annibale"]

lunghezza = {nome: "Lungo" if len(nome) > 5 else "corto" for nome in nomi}

print(lunghezza)