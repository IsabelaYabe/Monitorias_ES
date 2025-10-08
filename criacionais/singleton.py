def singleton(cls):
    """
    Decorador singleton
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            print(f"Criando instância única de {cls.__name__}")
            instances[cls] = cls(*args, **kwargs)
        else:
            print(f"Reutilizando instância existente de {cls.__name__}")
        return instances[cls]

    return get_instance

@singleton
class Classe:
    def __init__(self, nome):
        self.name = nome

a = Classe("classe_0")
b = Classe()

print(a is b)        
print(f"Nome de a: {a.name}")
print(f"Nome de b: {b.name}")       

b.name = "classe_1"
print(f"Trocando nome de b e mostrando nome de a: {a.name}")       
