from models.comprovante import Comprovante
from models.pagamento import Pagamento

# HERANÇA: Cartao herda os atributos e métodos de Pagamento.
# Também implementa o contrato definido por Comprovante.
class Cartao(Pagamento, Comprovante):
    JUROS = 0.10

    def __init__(self, valor, parcelas=1):
        # HERANÇA: super() chama o construtor da classe mãe Pagamento,
        # reutilizando sua inicialização.
        super().__init__(valor)
        if parcelas < 1 or parcelas > 12:
            raise ValueError("O cartão aceita de 1 a 12 parcelas.")
        self.__parcelas = parcelas

    @property
    def parcelas(self):
        return self.__parcelas

    def calcular_total(self):

        if self.__parcelas > 3:    #
            return round(self._valor * (1 + Cartao.JUROS), 2)
        return round(self._valor, 2)

    def descricao(self):
        return f"Cartão em {self.__parcelas}x"

    def gerar_comprovante(self):
        valor_parcela = round(self.calcular_total() / self.__parcelas, 2)
        return (
            f"Comprovante Cartão: R$ {self.calcular_total():.2f} "
            f"em {self.__parcelas}x de R$ {valor_parcela:.2f}."
        )
