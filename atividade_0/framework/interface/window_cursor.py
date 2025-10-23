from abc import ABC, abstractmethod

class Window(ABC):
    @abstractmethod
    def create_window(self): ...

class Cursor(ABC):
    @abstractmethod
    def create_cursor(self): ...
