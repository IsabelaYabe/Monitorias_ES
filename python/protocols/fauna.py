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
    
