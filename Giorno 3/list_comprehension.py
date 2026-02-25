numeri = [10,20,30,40]

nuovi = [num + 5 for num in numeri]

print(nuovi)

nomi = ["anna","luca","ciccio"]

maiuscoli = [nome.title() for nome in nomi]
print(maiuscoli)

#filtrare con lc
numeri_2 = [1,2,3,4,5,6,7,8,9,10]
pari = [numero for numero in numeri_2 if numero%2==0]
print(pari)

#trasf+filtraggio

pari10 = [numero*10 for numero in numeri_2 if numero%2==0]

print(pari10)