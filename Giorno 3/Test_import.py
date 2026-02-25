import utils as u

a = 3
b = 5

try:
    c = float(input("Inserisci numero naturale: "))
    print(u.divisione(a, c))
except ValueError:
    print("Brutto scemo ho detto un numero naturale naturale")
except ZeroDivisionError as e:
    print(e)
finally:
    print("E infine arriva ciccio cazzzo")

print(u.somma(a,b))
print(u.sottrazioni(a,b))
print(u.moltiplicazioni(a,b))

