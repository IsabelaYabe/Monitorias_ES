from logger import logger

class Contador:
    """
    Simple iterator that counts from 1 to n.
    """

    def __init__(self, n):
        self.n = n      
        self.atual = 0    

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual < self.n:
            self.atual += 1
            return self.atual
        else:
            self.atual = 0  
            raise StopIteration

def main():
    """Demonstration of the Contador iterator."""
    contador = Contador(5)
    
    logger.debug("Counting:")
    for numero in contador:
        logger.info(numero)
        
    logger.debug("Counting again:")
    for numero in contador:
        logger.info(numero)

if __name__ == "__main__":
    main()