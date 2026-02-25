"""
def dividi(a,b):
    if b==0:
        raise ZeroDivisionError("Il divisore non può essere 0")
    return a/b

try:
    print(dividi(2,3))
except ZeroDivisionError:
    print("Il divisore non può essere 0")


#errore custom
"""
class ErroreCustom(Exception):
    pass

#ora puoi dire
def dividi_sbag(a,b):
    if b==7:
        raise ErroreCustom("Che schifo il 7")
    return a/b

try:
    print(dividi_sbag(2, 7))
except ErroreCustom:
    print("Noneeee")

