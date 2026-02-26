f = open("dati.txt", "r")

print(f.read())
f.close()


#forma consigliata è

#with chiude in automatico il file!!!

with open("dati.txt", "r") as f:
    contenuto = f.read()

print(contenuto)
#print(f.read()) qua non funziona mica!Ormai è chiuso il file

#Leggere un file riga per riga

with open("dati.txt", "r") as f:
    contenuto_singolo = f.readlines()

for line in contenuto_singolo:
    print(line) #vede riga una per una !