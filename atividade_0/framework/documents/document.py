from __future__ import annotations

from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def is_open(self) -> bool:
        ...

    @abstractmethod
    def open(self) -> "Document":
        ...

    @abstractmethod
    def close(self) -> None:
        ...
