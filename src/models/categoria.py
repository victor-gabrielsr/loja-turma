class Categoria:
    def __init__(self, nome):

        self.__nome = ""
        self.renomear(nome)
    @property
    def nome(self):
        return self.__nome

    def renomear(self, nome):
        nome = nome.strip()
        if nome == "":
            raise ValueError("O nome da categoria não pode ser vazio.")
        self.__nome = nome

    def __str__(self):
        return self.__nome
