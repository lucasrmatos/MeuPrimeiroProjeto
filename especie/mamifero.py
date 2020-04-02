from animal import animal


class mamifero(animal):

    def __init__(self, tipo, peso, locomocao, idade):
        super().__init__(tipo, peso, locomocao, idade)


    def EmitirSom(self):
        print('Som de Mamifero')

