from .document import Document

class TextDocument(Document):
    def __init__(self, name: str):
        self.name = name
        self.content: str = None
        self.is_open: bool = False
        self._snapshot = None

    def _status(self):
        

    def open(self):
        self.is_open = True
        print(f"Abrindo o documento de texto '{self.name}'.")

    def close(self):
        self.is_open = False
        print(f"Fechando '{self.name}'.")

    def save(self):
        print(f"Salvando '{self.name}' com conteúdo: {self.content}")

    def revert(self):
        self.content = ""
        print(f"Revertendo '{self.name}' para o estado inicial.")
