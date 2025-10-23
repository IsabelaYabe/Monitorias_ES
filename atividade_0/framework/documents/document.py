from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

class Document(ABC):
    def __init__(self, name: str):
        self._name: str = name
        self._is_open: bool = name
        self._snapshot: Optional[Dict[str, Any]] = None

    @property
    def name (self) -> str:
        return self._name
    @name.setter
    def name(self, new_name) -> None:
        self._name = new_name

    @abstractmethod
    def _open(self): ...
    
    @abstractmethod
    def _close(self): ...
    
    @abstractmethod
    def save(self): ...
    
    @abstractmethod
    def revert(self): ...
