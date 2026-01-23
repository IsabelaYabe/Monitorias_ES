from __future__ import annotations

from abc import ABC, abstractmethod
from functools import wraps
from typing import Any, Dict

from ..documents import Document
from ..interface import InterfaceFactory
from ..singleton import SingletonABCMeta

DocumentFolder = Dict[str, Document]

class Application(ABC, metaclass=SingletonABCMeta):
    def __init__(self, ui: InterfaceFactory):
        self.ui: InterfaceFactory = ui
        self._document_folder: DocumentFolder = {}

    def new_document(self, name: str) -> Document:
        if name in self._document_folder:
            print(f"Reusing existing instance for '{name}'")
            doc = self._document_folder[name]
            self.open_document(name)
            return doc

        print(f"Creating new document '{name}'")
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

        if not doc.is_open:
            doc.open()
        else:
            print(f"'{name}' is already open")
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
        ...
