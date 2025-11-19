from abc import ABC, abstractmethod
from typing import List

class Unit(ABC):
    def __init__(self, name: str, level_state: "LevelState"):
        self.name = name
        self.level_state = level_state   

    @abstractmethod
    def accept(self, visitor: "UnitVisitor") -> None:
        pass

    def level_up(self) -> None:
        current_level = self.level_state.name
        self.level_state = self.level_state.next_level()
        if self.level_state.name != current_level:
            print(f"{self.name} subiu para {self.level_state.name}")

class Archer(Unit):
    def accept(self, visitor: "UnitVisitor") -> None:
        visitor.visit_archer(self)


class Cavalry(Unit):
    def accept(self, visitor: "UnitVisitor") -> None:
        visitor.visit_cavalry(self)


class Spearman(Unit):
    def accept(self, visitor: "UnitVisitor") -> None:
        visitor.visit_spearman(self)


class UnitGroup(Unit):
    def __init__(self, name: str, level_state: "LevelState"):
        super().__init__(name, level_state)
        self._children: List[Unit] = []

    def add(self, unit: Unit) -> None:
        self._children.append(unit)

    def remove(self, unit: Unit) -> None:
        self._children.remove(unit)

    def get_children(self) -> List[Unit]:
        return list(self._children)

    def accept(self, visitor: UnitVisitor) -> None:
        print(f"\n[{self.name}] executando ação para o grupo inteiro:")
        for child in self._children:
            child.accept(visitor)

    def level_up(self) -> None:
        super().level_up()
        for child in self._children:
            child.level_state = self.level_state

class UnitVisitor(ABC):
    @abstractmethod
    def visit_archer(self, archer: Archer) -> None: ...
    @abstractmethod
    def visit_cavalry(self, cavalry: Cavalry) -> None: ...
    @abstractmethod
    def visit_spearman(self, spearman: Spearman) -> None: ...

class AttackAction(UnitVisitor):
    def visit_archer(self, archer: Archer) -> None:
        print(f"{archer.name} dispara uma flecha normal.")

    def visit_cavalry(self, cavalry: Cavalry) -> None:
        print(f"{cavalry.name} avança com a espada.")

    def visit_spearman(self, spearman: Spearman) -> None:
        print(f"{spearman.name} perfura com a lança.")
        
class MoveAction(UnitVisitor):
    def visit_archer(self, archer: Archer) -> None:
        print(f"{archer.name} se reposiciona atrás das tropas.")

    def visit_cavalry(self, cavalry: Cavalry) -> None:
        print(f"{cavalry.name} faz uma carga pelo flanco.")

    def visit_spearman(self, spearman: Spearman) -> None:
        print(f"{spearman.name} avança protegendo a linha de frente.")

class SpecialAttackAction(UnitVisitor):
    def visit_archer(self, archer: Archer) -> None:
        print(f"{archer.name} prepara um tiro especial...")
        archer.level_state.special_attack(archer)

    def visit_cavalry(self, cavalry: Cavalry) -> None:
        print(f"{cavalry.name} abaixa a lança para um golpe especial...")
        cavalry.level_state.special_attack(cavalry)

    def visit_spearman(self, spearman: Spearman) -> None:
        print(f"{spearman.name} concentra energia na lança...")
        spearman.level_state.special_attack(spearman)