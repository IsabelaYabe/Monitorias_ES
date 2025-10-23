from abc import ABC, abstractmethod

class Window(ABC):
    @abstractmethod
    def draw(self): ...

class Cursor(ABC):
    @abstractmethod
    def move(self): ...
