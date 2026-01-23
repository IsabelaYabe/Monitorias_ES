from __future__ import annotations
from dataclasses import dataclass

from .document import Document
from .memento import Memento

@dataclass(frozen=True)
class TextState:
    content: str
    font: str
    font_size: int
    
class TextDocument(Document[TextState]):
    def __init__(self, name: str):
        super().__init__(name)
        self.content: str = ""
        self.font: str = "Arial"
        self.font_size: int = 12

    def write(self, text: str) -> None:
        if not self.is_open:
            raise ValueError(f"Document '{self.name}' is not open")
        self.content += text
        print(f"Updating document '{self.name}'\nContent: {self.content}")

    def _create_memento(self) -> Memento[TextState]:
        return Memento(TextState(self.content, self.font, self.font_size))

    def _restore_memento(self, memento: Memento[TextState]) -> None:
        st = memento.state
        self.content = st.content
        self.font = st.font
        self.font_size = st.font_size
        print(f"Reverted document '{self.name}' to previous state")