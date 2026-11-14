#Classe produto criada
# Associação: os produtos podem ser relacionados aos clientes
# por meio dos carrinhos utilizados no processo de compra.

class Produto:
    #Definindo os atributos que a classe produto vai ter
    def __init__(self, nome, preco, estoque, categoria):
        #privado(__) quer dizer que so a propria classe pode acessar 
        self.__nome = nome
        self.__preco = 0.0
        self.__categoria = categoria

        #Regras de negocio
        #Preco tem que ser maior que zero e nao pode ser menor que zero
        self.alterar_preco(preco)
        #O estoque segue a mesma logica nao podemos ter -1 de quantidade em um objeto real
        if estoque < 0:
            raise ValueError("O estoque não pode ser negativo.")
        self.__estoque = estoque

    #Definindo construtores
    #definir um método construtor é necessário para garantir que um objeto nasça com um estado inicial válido e pronto para ser usado
    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def estoque(self):
        return self.__estoque

    @property
    def categoria(self):
        return self.__categoria
    #O primeiro parametro(self) e o objeto que executa ess acao
    def alterar_preco(self, valor):
        #Esse metodo so muda o estado de valor seguindo a seguinte condicao
        if valor <= 0:
            raise ValueError(f"Preço inválido para {self.__nome}: precisa ser maior que zero.")
        self.__preco = float(valor)

    def tem_estoque(self, quantidade):
        return self.__estoque >= quantidade

    #Nao deixa dar baixa no estoque se a quantidade solicitada for maior do que o disponivel no estoque
    def baixar_estoque(self, quantidade):
        if not self.tem_estoque(quantidade):
            raise ValueError(
                f"Estoque insuficiente de {self.__nome}: há {self.__estoque} unidade(s)."
            )
        self.__estoque -= quantidade
    #Regra de nogocio
    #Nao tem como quantidade de reposicao do codigo ser menor que 0
    def repor_estoque(self, quantidade):
        if quantidade <= 0: 
            raise ValueError("A quantidade para repor precisa ser maior que zero.")
        self.__estoque += quantidade

    #Esse metodo vai ser chamado na main para exibir os objetos criados
    def __str__(self):
        return f"{self.__nome} - R$ {self.__preco:.2f} ({self.__estoque} em estoque) [{self.__categoria}]"

