from abc import ABC, abstractmethod

class InterfaceFactory(ABC):
    """Abstract Factory creates families of related objects."""
    
    @abstractmethod
    def create_window(self): ...

    @abstractmethod
    def create_cursor(self): ...
