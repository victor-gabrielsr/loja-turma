from models.item_carrinho import ItemCarrinho
class Carrinho:

    def __init__(self):
        self.__itens = []    # lista de objetos ItemCarrinho

    @property
    def itens(self):
        return list(self.__itens)

    def __buscar_item(self, produto):
        for item in self.__itens:
            if item.produto is produto:
                return item
        return None

    def adicionar(self, produto, quantidade=1):
        if quantidade <= 0:
            raise ValueError("A quantidade precisa ser maior que zero.")

        item = self.__buscar_item(produto)
        quantidade_total = quantidade
        if item is not None:
            quantidade_total += item.quantidade

        if not produto.tem_estoque(quantidade_total):     
            raise ValueError(
                f"Só há {produto.estoque} unidade(s) de {produto.nome} em estoque."
            )

        if item is not None:
            item.aumentar(quantidade)                          
        else:
             # Composição: o carrinho cria e armazena objetos ItemCarrinho,
             # que representam os itens que fazem parte da sua estrutura.
            self.__itens.append(ItemCarrinho(produto, quantidade))

    def remover(self, produto):

        item = self.__buscar_item(produto)
        if item is None:
            raise ValueError(f"{produto.nome} não está no carrinho.")
        self.__itens.remove(item)

    def total(self):

        soma = 0.0
        for item in self.__itens:
            soma += item.subtotal()
        return round(soma, 2)

    def esta_vazio(self):
        return len(self.__itens) == 0

    def limpar(self):

        self.__itens = []

    def __str__(self):
        if self.esta_vazio():
            return "Carrinho vazio."
        linhas = []
        for item in self.__itens:
            linhas.append(str(item))
        linhas.append(f"TOTAL: R$ {self.total():.2f}")
        return "\n".join(linhas)