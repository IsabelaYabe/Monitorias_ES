from __future__ import annotations

from typing import Any, Dict, Optional

from .document import Document


class TextDocument(Document):
    def __init__(self, name: str):
        super().__init__(name)
        self._is_open: bool = False

        self.content: str = ""
        self.font: str = "Arial"
        self.font_size: int = 12

        # Snapshot simples (tipo “memento”)
        self._snapshot: Optional[Dict[str, Any]] = None

    @property
    def is_open(self) -> bool:
        return self._is_open

    def open(self) -> "TextDocument":
        if self._is_open:
            return self
        self._is_open = True
        print(f"Opening document '{self.name}'")
        return self

    def close(self) -> None:
        if not self._is_open:
            return
        self._is_open = False
        print(f"Closing document '{self.name}'")

    def _state(self) -> Dict[str, Any]:
        return {
            "content": self.content,
            "font": self.font,
            "font_size": self.font_size,
        }

    def save(self) -> None:
        self._snapshot = self._state()
        print(f"Saving document '{self.name}'")

    def revert(self) -> None:
        if self._snapshot is None:
            print(f"No snapshot to revert for '{self.name}'")
            return

        self.content = self._snapshot["content"]
        self.font = self._snapshot["font"]
        self.font_size = self._snapshot["font_size"]
        print(f"Reverting document '{self.name}'")

    def read(self) -> None:
        if not self._is_open:
            raise ValueError(f"Document '{self.name}' is not open")
    
        return self.content

    def write(self, text: str) -> None:
        if not self._is_open:
            raise ValueError(f"Document '{self.name}' is not open")
        
        self.content += text
        print(f"Updating document '{self.name}'\nContent: {self.content}")
