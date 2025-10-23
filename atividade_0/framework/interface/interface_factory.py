from abc import ABC, abstractmethod

class InterfaceFactory(ABC):
    """Abstract Factory — cria famílias de objetos relacionados."""
    
    @abstractmethod
    def create_window(self): ...

    @abstractmethod
    def create_cursor(self): ...
