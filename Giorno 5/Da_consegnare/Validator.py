from Richiesta import Richiesta

class Validator(Richiesta):

    def validazione_eta(self):
        if self.eta >= 18:
            self.validita_eta = True
        else:
            self.validita_eta = False

    def validazione_nome(self):
        if self.nome == "":
            self.validita_nome = False
        else:
            self.validita_nome = True

    def validazione_email(self):
        if "@" in self.email:
            self.validita_email = True
        else:
            self.validita_email = False

    def sanificazione_dati(self):
        self.nome = self.nome.strip().title()
        self.email = self.email.strip()
        self.servizio = self.servizio.strip().lower()