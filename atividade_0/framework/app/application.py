from __future__ import annotations

from abc import ABC, abstractmethod
from functools import wraps
from typing import Any, Dict

from ..documents import Document
from ..interface import InterfaceFactory
from ..singleton import SingletonABCMeta

DocumentFolder = Dict[str, Document]


def multiton(key_arg: str, attr_name: str):
    @wraps(multiton)
    def decorador(func):
        @wraps(func)
        def get_instance(self, *args, **kwargs):
            if key_arg in kwargs:
                key = kwargs[key_arg]
            elif len(args) >= 1:
                key = args[0]
            else:
                raise ValueError(f"Could not find argument '{key_arg}'")

            instances = getattr(self, attr_name)

            if key in instances:
                print(f"Reusing existing instance for '{key}'")
                return instances[key]

            print(f"Creating new instance for '{key}'")
            created = func(self, *args, **kwargs)

            # Se o método não registrou (segurança), registra aqui.
            instances.setdefault(key, created)
            return instances[key]
        return get_instance
    return decorador


class Application(ABC, metaclass=SingletonABCMeta):
    def __init__(self, ui: InterfaceFactory):
        self.ui: InterfaceFactory = ui
        self._document_folder: DocumentFolder = {}

    @multiton("name", "_document_folder")
    def new_document(self, name: str) -> Document:
        """Factory Method + Multiton"""
        doc = self._create_document(name)

        self._document_folder[name] = doc

        self.open_document(name)
        return doc

    def show_ui(self) -> None:
        window = self.ui.create_window()
        cursor = self.ui.create_cursor()

        window.create_window()
        cursor.create_cursor()

    def open_document(self, name: str) -> Document:
        doc = self._document_folder.get(name)
        if doc is None:
            raise ValueError(f"Document '{name}' not found")

        self.show_ui()

        if doc.is_open:
            print(f"'{name}' is already open")
            return doc

        doc.open()
        return doc

    def close_document(self, name: str) -> None:
        doc = self._document_folder.get(name)
        if doc is None:
            raise ValueError(f"Document '{name}' not found")

        if not doc.is_open:
            print(f"'{name}' is already closed")
            return

        doc.close()

    @abstractmethod
    def _create_document(self, name: str) -> Document:
        """Factory Method"""
        raise NotImplementedError
