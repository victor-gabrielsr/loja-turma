from models.comprovante import Comprovante
from models.pagamento import Pagamento

# HERANÇA: Pix herda os atributos e métodos de Pagamento.
# Também implementa o contrato definido por Comprovante.
class Pix(Pagamento, Comprovante):
    """
    HERANÇA: Pix É UM Pagamento.
    INTERFACE: Pix também implementa o contrato Comprovante.
    """

    DESCONTO = 0.05    # RN8: Pix tem 5% de desconto

    def calcular_total(self):
        # SOBREPOSIÇÃO: mesmo nome do método da classe mãe, cálculo próprio
        return round(self._valor * (1 - Pix.DESCONTO), 2)

    def descricao(self):
        return "Pix (5% de desconto)"

    def gerar_comprovante(self):
        return f"Comprovante Pix: R$ {self.calcular_total():.2f} pagos à vista."
