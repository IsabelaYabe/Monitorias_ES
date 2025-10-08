from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def pagamento(self, value: float):
        """Processa um pagamento em reais (BRL)."""
        print("Pagamento efetuado")

class EUR_BRL(Pagamento)

