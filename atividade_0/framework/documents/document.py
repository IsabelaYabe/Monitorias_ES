from abc import ABC, abstractmethod

class Document(ABC):
    """Define o contrato para todos os tipos de documentos."""
    
    @abstractmethod
    def open(self): ...
    
    @abstractmethod
    def close(self): ...
    
    @abstractmethod
    def save(self): ...
    
    @abstractmethod
    def revert(self): ...
