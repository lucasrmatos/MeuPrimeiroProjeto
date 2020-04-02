from animais.animal import animal

class Ave(animal):
    def __init__(self, tipo, peso, locomocao, idade):
        super().__init__(tipo,peso,locomocao,idade)

    def EmitirSom(self):
        print('som de Ave')
