def somma(a,b):
    return a+b

def sottrazioni(a,b):
    return a-b

def moltiplicazioni(a,b):
    return a*b

def divisione(a,b):
    if b==0:
        raise ZeroDivisionError("Stai mettendo b = 0 maledetto")
    return a/b