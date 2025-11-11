from typing import Protocol, runtime_checkable

@runtime_checkable
class MySequence[T](Protocol):
    def __getitem__(self, index: int) -> T:
        ...

    def __len__(self) -> int:
        ...

# Função genérica: recebe qualquer "sequência" e devolve o primeiro elemento
def first(seq: MySequence[T]) -> T:
    return seq[0]

if __name__ == "__main__":
    nomes = ["Ana", "Bruno", "Carla"] # list[str]
    numeros = (1, 2, 3, 4)            # tuple[int, ...]

    print(first(nomes)) # -> "Ana"
    print(first(numeros)) # -> 1

    # Só pra mostrar que Protocol também pode ser checado em runtime:
    print(isinstance(nomes, MySequence))    # True
    print(isinstance(numeros, MySequence))  # True
