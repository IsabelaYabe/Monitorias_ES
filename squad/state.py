from abc import ABC, abstractmethod
from visitor import Unit

class LevelState(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def special_attack(self, unit: Unit) -> None:
        ...

    @abstractmethod
    def next_level(self) -> "LevelState":
        ...

class Level1(LevelState):
    @property
    def name(self) -> str:
        return "Level 1"

    def special_attack(self, unit: Unit) -> None:
        print(f"[{self.name}] {unit.name} usa um especial fraco (x1.2 de dano).")

    def next_level(self) -> "LevelState":
        return Level2()


class Level2(LevelState):
    @property
    def name(self) -> str:
        return "Level 2"

    def special_attack(self, unit: Unit) -> None:
        print(f"[{self.name}] {unit.name} usa especial em área (x1.5 de dano).")

    def next_level(self) -> "LevelState":
        return Level3()


class Level3(LevelState):
    @property
    def name(self) -> str:
        return "Level 3 (MAX)"

    def special_attack(self, unit: Unit) -> None:
        print(f"[{self.name}] {unit.name} usa ULTIMATE (x2.0 de dano)!!")

    def next_level(self) -> "LevelState":
        print(f"[Já está no nível máximo.")
        return self
