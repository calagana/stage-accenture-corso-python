#pipeline che
#riceve lista di strighe numeriche ["3", "5"...], converte in interi gestendo errori
#restituisce solo i > 10
#calcola la somma (nel for usa except con pass)

def ricevi_stringa():

    print("Inserisci un numero. Per segnalare la fine della stringa scrivi 'n'")

    lista_numeri = []

    while True:
        numero = input("Inserisci un numero: ")
        if numero == "n":
            break
        else:
            lista_numeri.append(numero)

    print("Lista finita, grazie.")
    print("Lista inserita: ", lista_numeri)
    return lista_numeri

def converti_str_int(lista_stringhe):
    lista_numeri = []
    for stringa in lista_stringhe:
        try:
            numero = float(stringa)
            lista_numeri.append(numero)
        except ValueError:
            print(stringa, "non può essere convertito e non sarà quindi considerato")
            pass

    print("Lista considerata: ", lista_numeri)
    return lista_numeri

def filtraggio(lista_numeri):

    numeri_filtrati = [numero for numero in lista_numeri if numero > 10]

    print("Lista filtrata: ", numeri_filtrati)

    return numeri_filtrati

def report_somma(lista_numeri):
    return sum(lista_numeri)



lista_stringhe = ricevi_stringa()

try:
    lista_numeri = converti_str_int(lista_stringhe)
except:
    print("Qualcosa è andato storto.")
else:
    numeri_filtrati = filtraggio(lista_numeri)
    somma = report_somma(numeri_filtrati)

    print("La somma dei tuoi numeri è", somma)