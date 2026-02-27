
class Richiesta():

    def __init__(self,id,nome,email,eta,servizio):
        self.id = id
        self.nome = nome
        self.email = email
        self.eta = eta
        self.servizio = servizio

    def restituisci_dizionario(self):

        # Definisco un dizionario per poterlo usare successivamente
        diz = {}
        diz["id"] = self.id
        diz["nome"] = self.nome
        diz["email"] = self.email
        diz["eta"] = self.eta
        diz["servizio"] = self.servizio

        return diz