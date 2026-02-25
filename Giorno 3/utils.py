def somma(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("Somma, a, b, devono essere int")
    return a+b

def sottrazioni(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("Somma, a, b, devono essere int")
    return a-b

def moltiplicazioni(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("Somma, a, b, devono essere int")
    return a*b

def divisione(a,b):
    if b==0:
        raise ZeroDivisionError("Stai mettendo b = 0 maledetto")
    return a/b

def erroralo():
    raise ErroreCustom("Hai detto di dirti che hai sbagliato")