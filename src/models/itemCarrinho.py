class itemCarrinho:
    def __init__(self, quantidade, produto):
        self.__quantidade = quantidade
        self.__produto = produto
        self.adcionar (quantidade)
        self.subtotal = 0
        pass
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    def adcionar(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Adicionar produto!")
        self.__quantidade
        
    def subtotal(self):
        return self.__produto.preco * self.__quantidade
    
    def __str__(self):
        return f"{self.__produto.nome}x{self.__quantidade} = R$ {self.subtotal():.2f}"
        pass