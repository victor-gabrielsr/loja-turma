class Categoria:
    #definindo atributos
    def __init__(self, nome):
        self.__nome = nome

    #Definindo propriedade e metodo para atributo nome
    @property
    def nome(self):
        return self.__nome

    def renomear(self, nome):
        nome = nome.strip()
        if nome == "":
            raise ValueError("O nome não pode ser vazio!!!")

    def __str__(self):
        return f"{self.__nome}"
