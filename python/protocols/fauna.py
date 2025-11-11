from typing import Protocol

class Walker(Protocol):
    def walk(self, destination: str) -> None:
        ...

    def run(self, destination: str) -> None:
        ...

class Swimmer(Protocol):
    def swim(self, destination: str) -> None:
        ...

    def dive(self, depth: float) -> None:
        ...

def underwater_exploration(entity: Swimmer) -> None:
    entity.dive(50)
    entity.swim("shipwreck")

class Whale: 
    """
    It's a Swimmer?
    """
    def dive(self, depth: float) -> None:
        print(f"Whale is diving to {depth = }.")

    def swim(self, destination: str) -> None:
        print(f"Whale is swimming to {destination = }.")

mobby_dick = Whale()
underwater_exploration(mobby_dick) 
