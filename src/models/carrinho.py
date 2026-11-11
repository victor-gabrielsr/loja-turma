from models.itemCarrinho import itemCarrinho

class Carrinho:
    def __init__(self, itens):
        self.__itens = []

    @property
    def itens(self):
        return self.__itens

    def adicionar(self, produto, quantidade):
        for itens in self.__itens:
            if itens.produto == produto:
                self.__itens.remove(itens)

    def remover(self, produto):
        if itens.produto == produto:
            self.__itens.remove(self.itens)

    def total(self):
        return sum(item.subtotal() for item in self.__itens)
    
    def esta_vazio(self):
        if len(self.itens) == 0:
            return  True
        
    def limpar(self):
        self.itens.clear()
        