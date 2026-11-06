from models.categoria import Categoria
from models.produto import Produto

eletronicos = Categoria ("Eletrônicos")
mouse = Produto("Mouse", 2, 2, "Eletrônicos")

print(mouse)