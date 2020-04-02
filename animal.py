from abc import ABC

class animal():

    def __init__(self,tipo,peso,locomocao,idade):
        self.tipo = tipo
        self.peso = peso
        self.locomocao = locomocao
        self.idade = idade
    

class mamifero(animal):

    def __init__(self, tipo, peso, locomocao, idade):
        super().__init__(tipo, peso, locomocao, idade)


    def EmitirSom(self):
        print('Som de Mamifero')


class Ave(animal):
    def __init__(self, tipo, peso, locomocao, idade):
        super().__init__(tipo,peso,locomocao,idade)

    def EmitirSom(self):
        print('som de Ave')


