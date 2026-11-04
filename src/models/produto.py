#classe produto

#definindo classe produto
class produto():
    def __init__(self, nome, preco, estoque):
        
        self.__nome = nome
        self.__preco = 0.0
        self.__estoque = 0

        self.alterar_preco(preco)
        if preco < 0:
            print("Prço não pode ser negativo!")

        self.baixar_estoque(estoque)
        if estoque < 0:
             print("O valor do estoque não pode ser negativo!")

        self.repor_estoque(estoque)
# definindo metodo alterar preco

        def aletrar_preco(self, valor):
            if valor < 0:
                print("Preço inválido!")
            self.__preco = float(valor)

        def baixar_estoque(self, quantidade):
            if quantidade < 0:
                print("Não tem estoque!")
            self.__quantidade = int(quantidade)

        def repor_estoque(self, quantidade):
            self.__estoque += quantidade        
        
        
        pass