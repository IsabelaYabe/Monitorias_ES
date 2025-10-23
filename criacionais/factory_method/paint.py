from . import Document, Application
from typing import Dict, Any, Optional
import copy

class Drawing(Document):
    def __init__(self, name: str):
        super().__init__(name)
        self._content: Optional[str] = None
        self._colors: Optional[list[str]] = None

    @property
    def content(self) -> str:
        return self._content
    @content.setter
    def content(self, content: str):
        self._content = content
    @property
    def colors(self) -> list[str]:
        return self._colors
    @colors.setter
    def colors(self, colors: list[str]):
        self._colors = colors
    
    def _open(self) -> None:
        self._is_open = True
        print(f"Opening document '{self._name}'.")
        print(f"Content: {self._content}")
        print(f"Colors: {self._colors}")
    
    def _close(self) -> None:
        self._is_open = False
        print(f"Closing drawing '{self._name}'")

    def _state(self) -> Dict[str, Any]:
        content = copy.deepcopy(self._content)
        colors = copy.deepcopy(self._colors)
        state = {}
        state["content"] = content
        state["colors"] = colors
        print(f"Capturing state for drawing '{self._name}'")
        return state

    def save(self) -> None:
        self._snapshot = self._state()
        print(f"Saved drawing '{self._name}'")

    def revert(self) -> None:
        if self._snapshot is not None:
            self._content = self._snapshot["content"]
            self._colors = self._snapshot["colors"]
            print(f"Reverted drawing '{self._name}' to last saved state")
        else:
            print(f"No saved state to revert to for drawing '{self._name}'")

class Paint(Application):
    def _create_document(self, name: str): 
        doc = Drawing(name)
        return doc
