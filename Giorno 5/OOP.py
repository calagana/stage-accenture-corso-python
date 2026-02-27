class libro:
    def __init__(self, nome, genere, n_pagine):
        self.nome = nome
        self.genere = genere
        self.n_pagine = n_pagine

    def presenta(self):
        print(f"Il libro '{self.nome}' ha {self.n_pagine} pagine ed è di genere {self.genere}")

    def lunghezza(self):
        if self.n_pagine > 600:
            print(f"'{self.nome}' è un libro veramente lungo caspita")
        else:
            print(f"'{self.nome}' è un libro veramente corto, che schifo")


got = libro("Il Trono di Spade", "Fantasy", 1000)
percy = libro("PJ", "Fantasy", 300)

got.presenta()
got.lunghezza()
percy.lunghezza()