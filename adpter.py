class Contador:
    """
    Iterador simples que conta de 1 até n.
    """

    def __init__(self, n):
        self.n = n      
        self.atual = 0    

    def __iter__(self):
        print("Chamando __iter__()")
        return self

    def __next__(self):
        print("Chamando __next__()")
        if self.atual < self.n:
            self.atual += 1
            return self.atual
        else:
            raise StopIteration
