import utils as u

a = 3
b = 3

try:
    c = float(input("Inserisci numero naturale: "))
    print(u.divisione(a, c))
except ValueError:
    print("Brutto scemo ho detto un numero naturale naturale")
except ZeroDivisionError as e:
    print(e)
finally:
    print("Ed ecco il finale")

print(u.somma(a,b))
print(u.sottrazioni(a,b))
print(u.moltiplicazioni(a,b))

