from __future__ import annotations

from typing import List
from .document import Document
from .memento import Memento

class TextDocument(Document):
    def __init__(self, name: str):
        super().__init__(name)
        self.content: str = ""
        self.font: str = "Arial"
        self.font_size: int = 12

    def write(self, text) -> None:
        if not self._is_open:
            raise ValueError(f"Document '{self.name}' is not open")
        self.content += text
        print(f"Updating document '{self.name}'\nContent: {self.content}")

    def _create_memento(self) -> Memento:
        return Memento(self.content, self.font, self.font_size)

    def _restore_memento(self, memento: Memento) -> None:
        self.content = memento.content
        self.font = memento.font
        self.font_size = memento.font_size
        print(f"Reverted document '{self.name}' to previous state")