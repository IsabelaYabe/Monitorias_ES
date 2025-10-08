from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def pay(self, value: float):
        """Processa um pagamento em reais (BRL)."""
        pass


