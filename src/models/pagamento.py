from abc import ABC, abstractmethod


# CLASSE ABSTRATA:
# A classe Pagamento herda de ABC, permitindo criar métodos abstratos.
class Pagamento(ABC):
    def __init__(self, valor):
        if valor <= 0:
            raise ValueError("O valor do pagamento precisa ser maior que zero.")
        self._valor = float(valor)

    @property
    def valor(self):
        return self._valor
    # MÉTODO ABSTRATO:
    # Obriga as classes filhas a implementar seu próprio cálculo do pagamento.
    @abstractmethod
    def calcular_total(self):
        """Cada forma de pagamento calcula o total do seu jeito."""

    # MÉTODO ABSTRATO:
    # Obriga as classes filhas a informar o nome da forma de pagamento.
    @abstractmethod
    def descricao(self):
        """Nome da forma de pagamento, para mostrar na tela."""

    