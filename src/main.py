# CLASSES: importamos as classes criadas nos arquivos do projeto
# para utilizá-las e instanciar seus respectivos objetos na main.
from models.cartao import Cartao
from models.categoria import Categoria
from models.cliente import Cliente
from models.pagamento import Pagamento
from models.pedido import Pedido
from models.pix import Pix
from models.produto import Produto

print("-="* 15)
print("     Produto")
print("-="* 15)

# OBJETOS: criamos instâncias das classes Categoria e Produto,
# cada uma com suas próprias características.
#Atribuindo eletronicos na classe categoria
eletronicos = Categoria("Eletronicos")
#Atribuindo teclado gamer e microfone na classe produto e passando os parametros
# ATRIBUTOS: passamos os valores de nome, preço, estoque
# e categoria para inicializar as características do produto.
tecladoGamer = Produto("Teclado gamer", 1000, 10, eletronicos)
microfone = Produto("Microfone", 150, 30, eletronicos)
print(tecladoGamer)
print(microfone)
#Chama a funcao baixar estoque simulando como se a pessoa estivesse comprando o teclado
tecladoGamer.baixar_estoque(5)
print("Estoque depois de baixar 5 (esperado 5):", tecladoGamer.estoque)
#Depois que a pessoa compra o estoque diminue entao a empresa repoes ele
tecladoGamer.repor_estoque(2)
print("Estoque depois de repor 2 (esperado 7):", tecladoGamer.estoque)

print("--- Categoria ---")

print("Categoria do notebook (esperado Eletronicos):", tecladoGamer.categoria)


eletronicos.renomear("Eletrônicos")
print("Depois de renomear (esperado Eletrônicos):", tecladoGamer.categoria)





print("--- Cliente e Carrinho ---")

victor = Cliente("Victor", "victor@email.com")
print(victor)
# MÉTODOS: chamamos métodos dos objetos para executar ações,
# como alterar estoque, adicionar produtos e confirmar pedidos.
victor.carrinho.adicionar(tecladoGamer, 1)
victor.carrinho.adicionar(microfone, 1)
victor.carrinho.adicionar(microfone, 1)    # RN5: repetido aumenta a quantidade
print(victor.carrinho)
print("Linhas no carrinho (esperado 2):", len(victor.carrinho.itens))
print("Total do carrinho (esperado 3700.0):", victor.carrinho.total())

print("--- Pagamento ---")
# POLIMORFISMO:
# Criamos diferentes objetos de pagamento, das classes Pix e Cartao.
pix = Pix(3700)
cartao_3x = Cartao(3700, 3)
cartao_6x = Cartao(3700, 6)

print("RN8 - Pix (esperado 3515.0):", pix.calcular_total())
print("RN9 - Cartão em 3x (esperado 3700.0):", cartao_3x.calcular_total())
print("RN9 - Cartão em 6x (esperado 4070.0):", cartao_6x.calcular_total())
# POLIMORFISMO:
# Armazenamos objetos de classes diferentes na mesma lista.
pagamentos = [pix, cartao_3x, cartao_6x]
# POLIMORFISMO:
# Chamamos o mesmo método para todos os objetos.
# Cada classe executa sua própria implementação de gerar_comprovante().
for pagamento in pagamentos:
    print(pagamento.gerar_comprovante())

print("--- Pedido ---")

pedido = Pedido(1, victor, "pix")
print("Total do pedido com Pix (esperado 3515.0):", pedido.total())

pedido.confirmar()
print(pedido)
print("RN11 - Estoque do notebook depois de confirmar (esperado 4):", tecladoGamer.estoque)
print("RN11 - Estoque do mouse depois de confirmar (esperado 18):", microfone.estoque)
print("RN7 - Carrinho depois do pedido (esperado Carrinho vazio.):", victor.carrinho)

pedido.cancelar()
print("RN11 - Estoque do notebook depois de cancelar (esperado 5):", tecladoGamer.estoque)
print("RN11 - Estoque do mouse depois de cancelar (esperado 20):", microfone.estoque)

