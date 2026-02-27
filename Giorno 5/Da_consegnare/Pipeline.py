class Pipeline:

    def __init__(self):
        pass

    def aggiungi_categoria_eta(self, richiesta):

        categoria = ""

        if richiesta.eta >= 40:
            categoria = "Senior"
        elif richiesta.eta >= 26:
            categoria = "Adult"
        elif richiesta.eta >= 18:
            categoria = "Junior"

        richiesta.categoria_eta = categoria

    def validazione_richiesta(self, richiesta):
        richiesta_valida = False

        if richiesta.validita_nome and richiesta.validita_eta and richiesta.validita_email:
            richiesta_valida = True