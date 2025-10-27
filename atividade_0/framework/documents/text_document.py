from .document import Document
from typing import Dict, Any
import copy

class TextDocument(Document):
    def __init__(self, name: str):
        super().__init__(name)
        self._content: str = None
        self._font: str = "Arial"
        self._font_size: int = 12
    
    @property
    def content(self) -> str:
        return self._content
    @content.setter
    def content(self, new_content: str) -> None:
        self._content = new_content
    @property
    def font(self) -> str:
        return self._font
    @font.setter
    def font(self, new_font: str) -> None:
        self._font = new_font
    @property
    def font_size(self) -> str:
        return self._font_size
    @font_size.setter
    def font_size(self, new_font_size: str) -> None:
        self._font_size = new_font_size    
    
    def _open(self):
        self._is_open = True
        print(f"Abrindo o documento de texto '{self.name}'.")

    def _close(self):
        self._is_open = False
        print(f"Fechando '{self.name}'.")
    
    def _state(self) -> Dict[str, Any]:
        content = copy.deepcopy(self._content)
        font = copy.deepcopy(self._font)
        font_size = copy.deepcopy(self._font_size)
        
        state: Dict[str, Any] = {}
        state["content"] = content
        state["font"] = font
        state["font_size"] = font_size
        print(f"Capturing state for text document '{self._name}'")
        return state
    
    def save(self) -> None:
        self._snapshot = self._state()
        print(f"Salvando '{self.name}'")

    def revert(self) -> None:
        if self._snapshot is None:
            print("No saved state to revert to for text document")
        
        self._content = self._snapshot["content"]
        self._font = self._snapshot["font"]
        self._font_size = self._snapshot["font_size"]
        print(f"Reverted '{self.name}' to last saved state")
