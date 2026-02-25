prezzi = [12.5, 9.9, 15, 7.5, 30]

#creo lista con prezzi maggiori di 10
prezzi10 = [prezzo for prezzo in prezzi if prezzo >10]
print(prezzi10)

numeri = [5,12,7,20,3,18]

#creare lista che divida per 2 i numeri maggiori di 10
#lasci invariati gli altri

modificati = [numero/2 if numero >10 else numero for numero in numeri]

print(modificati)