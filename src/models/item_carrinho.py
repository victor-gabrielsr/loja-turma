class ItemCarrinho:
    def __init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade

    @property
    def produto(self):
        return self.__produto

    @property
    def quantidade(self):
        return self.__quantidade

    def aumentar(self, quantidade):
        self.__quantidade += quantidade

    def subtotal(self):
        return round(self.__produto.preco * self.__quantidade, 2)

    def __str__(self):
        return f"{self.__quantidade}x {self.__produto.nome} = R$ {self.subtotal():.2f}"
