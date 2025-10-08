from abc import ABC, abstractmethod

class ConversorMoeda:
    """Classe para pegar valor do euro e do bitcoin e converter para real."""

class Pagamento(ABC):
    @abstractmethod
    def pagamento(self):
        """Processa um pagamento em reais (BRL)."""

class EUR_BRL(Pagamento):
    def __init__(self, euro: float):
        self._euro = euro
        self.real = None
        self.conversao = 7
        
    def _setter_real(self):
        self.real = (self.conversao) * (self._euro)
    
    def pagamento(self):
        self._setter_real()    
        return self.real

class BTC_BRL(Pagamento):
    def __init__(self, btc):
        self._btc = btc
        self.real = None
        self.conversao = 10000
        
    def _setter_real(self):
        self.real = (self.conversao) * (self._btc)
    
    def pagamento(self):
        self._setter_real()
        return self.real

euro = EUR_BRL(25)
btc = BTC_BRL(0.02)
pagamentos = [euro, btc]

for pag in pagamentos:
    pagg = pag.pagamento()
    print(pagg)
