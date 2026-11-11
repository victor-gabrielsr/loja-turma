from models.categoria import Categoria
from models.produto import Produto

<<<<<<< HEAD
eletronicos = Categoria ("Eletrônicos")
mouse = Produto("Mouse", 2, 2, "Eletrônicos")

=======
eletronicos = Categoria ("Eletronicos")
pesca = Categoria ("Pesca")
casa = Categoria ("")

mouse = Produto("mouse", 2, 2, "Eletronicos")

#mouse.tem_estoque(1)
#print(mouse)

mouse.baixar_estoque(1)
>>>>>>> upstream/main
print(mouse)