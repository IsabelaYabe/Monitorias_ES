from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

from .memento import Memento

TState = TypeVar("TState")

class Document(ABC, Generic[TState]):
    def __init__(self, name: str):
        self.name: str = name
        self._history: List[Memento[TState]] = []
        self._is_open: bool = False

    def save(self) -> None:
        if not self.is_open:
            raise ValueError(f"Document '{self.name}' is not open")
        
        self._history.append(self._create_memento())

    def revert(self) -> None:
        if not self._history:
            print(f"No previous state to revert to for document '{self.name}'")
            return
        self._restore_memento(self._history[-1])
        
    def undo(self) -> None:
        if not self._history:
            print(f"No previous state to undo for document '{self.name}'")
            return
        self._restore_memento(self._history.pop())

    @abstractmethod
    def _create_memento(self) -> Memento[TState]:
        ...

    @abstractmethod
    def _restore_memento(self, memento: Memento[TState]) -> None:
        ...

    @property
    def is_open(self) -> bool:
        return self._is_open
 
    def open(self) -> "Document[TState]":
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