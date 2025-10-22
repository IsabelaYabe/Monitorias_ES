from abc  import ABC, abstractmethod
from typing import Dict

class Document(ABC):
    @abstractmethod
    def open(self) -> None: ...

    @abstractmethod
    def close(self) -> None: ...

    @abstractmethod
    def save(self) -> None: ...

    @abstractmethod
    def revert(self) -> None: ...

class Application(ABC):
    def __init__(self) -> None: 
        self._docs: Dict[str, Document] = {}
    
    @abstractmethod
    def new_document(self, *args, **kwargs) -> Document: 
        """Factory Method Usage: create + register + open."""
        doc = self.create_document(*args, **kwargs)
        self._docs.append(doc)
        doc.open()
        return doc
    
    @abstractmethod
    def open_document(self, *args, **kwargs) -> Document: 
        doc = self.create_document(*args, **kwargs)
        self._docs.append(doc)    
        doc.open()
        return doc

    @abstractmethod
    def create_document(self, *args, **kwargs) -> Document: ... # Factory method
