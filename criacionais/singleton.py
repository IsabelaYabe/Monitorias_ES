def singleton(cls):
    """
    Decorador singleton
    """
    instances = {}

    def wrapper(*args, **kwargs):
        print(f"Instancias: {instances}")
        if cls not in instances.keys():
            print(f"Criando instância única de {cls.__name__}")
            instances[cls] = cls(*args, **kwargs) # aqui estamos instanciando a lixo
        else:
            print(f"Reutilizando instância existente de {cls.__name__}")
        return instances[cls]

    return wrapper

@singleton
class Lixo:
    def __init__(self, nome):
        self.name = nome

a = Lixo("lixo_0")
print("="*20)
b = Lixo("lixo_1")


print(a is b)        
print(f"Nome de a: {a.name}")
print(f"Nome de b: {b.name}")       

b.name = "lixo_1"
print(f"Trocando nome de b e mostrando nome de a: {a.name}")       
