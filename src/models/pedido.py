
from models.cartao import Cartao
from models.pix import Pix


class Pedido:

    def __init__(self, numero, cliente, forma_pagamento, parcelas=1):
        if cliente.carrinho.esta_vazio():  
            raise ValueError("O carrinho está vazio: não dá para fechar o pedido.")

        self.__numero = numero
        # AGREGAÇÃO:
        # O pedido recebe um objeto Cliente já existente
        # e mantém uma referência a ele.
        # O cliente pode existir independentemente do pedido.
        self.__cliente = cliente
        # RELACIONAMENTO COM OS ITENS:
        # O pedido recebe os itens presentes no carrinho do cliente.
        self.__itens = cliente.carrinho.itens
        self.__status = "aberto"

        if forma_pagamento == "pix":
            self.__pagamento = Pix(self.subtotal())
        elif forma_pagamento == "cartao":
            self.__pagamento = Cartao(self.subtotal(), parcelas)
        else:
            raise ValueError("Forma de pagamento inválida: use 'pix' ou 'cartao'.")

    @property
    def numero(self):
        return self.__numero

    @property
    def status(self):
        return self.__status

    @property
    def itens(self):
        return list(self.__itens)

    @property
    def pagamento(self):
        return self.__pagamento

    def subtotal(self):
        soma = 0.0
        for item in self.__itens:
            soma += item.subtotal()
        return round(soma, 2)
    # POLIMORFISMO:
    # O pagamento pode ser um objeto Pix ou Cartao.
    # O método calcular_total() executa a implementação
    # correspondente à classe do objeto armazenado.
    def total(self):
        return self.__pagamento.calcular_total()

    def confirmar(self):

        if self.__status != "aberto":
            raise ValueError(f"O pedido {self.__numero} já está {self.__status}.")

        for item in self.__itens:
            if not item.produto.tem_estoque(item.quantidade):
                raise ValueError(f"Estoque insuficiente de {item.produto.nome}.")
        for item in self.__itens:
            item.produto.baixar_estoque(item.quantidade)

        self.__status = "confirmado"
        self.__cliente.carrinho.limpar()          
        self.__cliente.adicionar_pedido(self)

    def cancelar(self):
        if self.__status != "confirmado":
            raise ValueError("Só dá para cancelar um pedido confirmado.")
        for item in self.__itens:
            item.produto.repor_estoque(item.quantidade)
        self.__status = "cancelado"

    def __str__(self):
        linhas = [f"Pedido {self.__numero} ({self.__status}) - {self.__cliente.nome}"]
        for item in self.__itens:
            linhas.append(f"  {item}")
            # POLIMORFISMO:
            # A descrição apresentada depende da forma de pagamento utilizada.
        linhas.append(f"  Subtotal: R$ {self.subtotal():.2f}")
        linhas.append(f"  Pagamento: {self.__pagamento.descricao()}")
        linhas.append(f"  TOTAL: R$ {self.total():.2f}")
        return "\n".join(linhas)

class Pedido:
    def __init__(self, numero, cliente, forma_pagamento, parcelas=1):
        self.__numero = numero
        self.__cliente = cliente