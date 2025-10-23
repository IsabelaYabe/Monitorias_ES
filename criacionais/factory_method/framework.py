from abc  import ABC, abstractmethod
from typing import Dict, Any, Optional

class Document(ABC):
    def __init__(self, name: str):
        self._name: str = name
        self._is_open: bool = False
        self._snapshot: Optional[Dict[str, Any]] = None

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name
    
    @abstractmethod
    def _open(self) -> None: ...

    @abstractmethod
    def _close(self) -> None: ...

    @abstractmethod
    def save(self) -> None: ...

    @abstractmethod
    def revert(self) -> None: ...

class Application(ABC):
    def __init__(self) -> None: 
        self._docs: Dict[str, Document] = {}
        
    def new_document(self, *args, **kwargs) -> Document: 
        """Factory Method Usage: create + register + open"""
        doc = self._create_document(*args, **kwargs) 
        self._docs[doc.name] = doc  
        self.open_document(doc.name)
        return doc
    
    def open_document(self, name) -> Document:
        if self._docs[name] is None:
            raise ValueError(f"Document '{name}' not found")
        
        doc = self._docs[name]
        if doc._is_open == True:
            print(f"'{name}' is already open")
            return doc    
        return doc._open()

    def close_document(self, name) -> None:
        if self._docs[name] is None:
            raise ValueError(f"Document '{name}' not found")
        
        doc = self._docs[name]
        if self._docs[name]._is_open == False:
            print(f"'{name}' is already closed")
        else:
            doc._close() 

    @abstractmethod
    def _create_document(self, *args, **kwargs) -> Document: ... # Factory method
