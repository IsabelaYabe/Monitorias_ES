from abc import ABC, abstractmethod
from functools import wraps

def multiton(id):
    def decorador(func):
        """ Decorator para implementar o padrão Multiton. """
        instances = {}

        @wraps(func)
        def get_instance(*args, **kwargs):
            if id in kwargs:
                key = kwargs[id]
            elif len(args) > 1:
                key = args[1]
            else:
                raise ValueError(f"Não foi possível encontrar o argumento '{id}'.")

            if key not in instances:
                print(f"Criando nova instância para '{key}'.")
                instances[key] = func(*args, **kwargs)
            else:
                print(f"Reutilizando instância existente para '{key}'")
            return instances[key]
        return get_instance
    return decorador
_
class Application(ABC):
    """Define o criador de documentos e controla instâncias (Multiton)."""
    
    def __init__(self):
        self._documents = {}
    
    @multiton("name")
    def new_document(self, name: str):
        """Factory Method + Multiton"""
        doc = self.create_document(name)
        self._documents[name] = doc
        doc.open()
        return doc

    @abstractmethod
    def create_document(self, name: str):
        """Factory Method"""
