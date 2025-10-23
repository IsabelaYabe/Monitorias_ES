from framework.documents import Document

from abc import ABC, abstractmethod
from functools import wraps
from typing import Dict, Any


def multiton(id: Any, attr_name: str):
    def decorador(func):
        """ Decorator para implementar o padrão Multiton. """
        @wraps(func)
        def get_instance(self, *args, **kwargs):
            if id in kwargs:
                key = kwargs[id]
            elif len(args) > 1:
                key = args[1]
            else:
                raise ValueError(f"Não foi possível encontrar o argumento '{id}'.")

            instances = getattr(self, attr_name)

            if key not in instances:
                print(f"Criando nova instância para '{key}'.")
                instances[key] = func(*args, **kwargs)
            else:
                print(f"Reutilizando instância existente para '{key}'")
            return instances[key]
        return get_instance
    return decorador

class Application(ABC):
    """Define o criador de documentos e controla instâncias (Multiton)."""
    
    def __init__(self):
        self._documents: Dict[str, Document] = {}
    
    @multiton("name", "_documents")
    def new_document(self, name: str):
        """Factory Method + Multiton"""
        doc = self.create_document(name)
        self._documents[name] = doc
        doc.open_document()
        return doc

    def open_document(self, name) -> Document:
        if self._docs[name] is None:
            raise ValueError(f"Document '{name}' not found")
        
        doc = self._documents[name]
        if doc._is_open == True:
            print(f"'{name} is alredy open")
            return doc
        return doc._open()
    
    def open_document(self, name) -> None:
        if self._documents[name] is None:
            raise ValueError(f"Document '{name}' not found")
        
        doc = self._documents[name]
        if doc._is_open == False:
            print(f"'{name} is alredy closed")
        else:
            doc._close()
    
    @abstractmethod
    def create_document(self, name: str):
        """Factory Method"""
