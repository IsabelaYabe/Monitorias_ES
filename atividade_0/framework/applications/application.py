from ..documents import Document
from ..interface import InterfaceFactory

from abc import ABC, abstractmethod
from functools import wraps
from typing import Dict, Any


def multiton(id: Any, attr_name: str):
    def decorador(func):
        """Decorator to implement the Multiton pattern"""
        @wraps(func)
        def get_instance(self, *args, **kwargs):
            if id in kwargs:
                key = kwargs[id]
            elif len(args) > 1:
                key = args[1]
            else:
                raise ValueError(f"Could not find argument '{id}'")

            instances = getattr(self, attr_name)

            if key not in instances:
                print(f"Creating new instance for '{key}'")
                instances[key] = func(self, *args, **kwargs)
            else:
                print(f"Reusing existing instance for '{key}'")
            return instances[key]
        return get_instance
    return decorador

class Application(ABC):
    def __init__(self, ui: InterfaceFactory):
        self.ui: InterfaceFactory = ui
        self._documents: Dict[str, Document] = {}
    
    @multiton("name", "_documents")
    def new_document(self, name: str):
        """Factory Method + Multiton"""
        doc = self.create_document(name)
        self._documents[name] = doc
        self.open_document(name)
        return doc

    def show_ui(self) -> None:
        window = self.ui.create_window()
        cursor = self.ui.create_cursor()

    def open_document(self, name) -> Document:
        if self._documents[name] is None:
            raise ValueError(f"Document '{name}' not found")
        
        self.show_ui()
        doc = self._documents[name]
        if doc._is_open == True:
            print(f"'{name} is alredy open")
            return doc
        return doc._open()
    
    def close_document(self, name) -> None:
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
