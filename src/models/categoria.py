class categoria():
    def __init__(self, nome):
        self.__nome = nome

        self.renomear(nome)

    def renomear(self, nome):
        nome = input("Digite o novo nome do produto: ")
