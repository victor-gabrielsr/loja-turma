
from abc import ABC, abstractmethod


# INTERFACE:
# Define um contrato que deve ser seguido pelas classes que herdarem dela.
class Comprovante(ABC):
    # MÉTODO ABSTRATO:
    # Obriga as classes filhas a implementarem a geração do comprovante.
    @abstractmethod
    def gerar_comprovante(self):
        """Devolve o texto do comprovante."""