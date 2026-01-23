from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from .memento import Memento

class Document(ABC):
    def __init__(self, name: str):
        self.name: str = name
        self._history: List[Memento] = []
        self._is_open: bool = False

    def save(self) -> None:
        self._history.append(self._create_memento())

    def revert(self) -> None:
        if not self._history:
            print(f"No previous state to revert to for document '{self.name}'")
            return
        popped_memento = self._history.pop()
        self._restore_memento(popped_memento)
        
    @abstractmethod
    def _create_memento(self) -> Memento:
        ...
    
    @abstractmethod
    def _restore_memento(self, memento: Memento) -> None:
        ...

    @property
    def is_open(self) -> bool:
        return self._is_open
 
    def open(self) -> "Document":
        if self._is_open:
            print(f"Document '{self.name}' is already open")
            return self
        self._is_open = True
        print(f"Opening document '{self.name}'")
        return self       

    def close(self) -> None:
        if not self._is_open:
            print(f"Document '{self.name}' is already closed")
            return
        self._is_open = False
        print(f"Closing document '{self.name}'")