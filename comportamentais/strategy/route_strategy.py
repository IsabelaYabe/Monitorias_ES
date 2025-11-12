from abc import ABC, abstractmethod
from typing import List

class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, origin: str, destination: str) -> List[str]:
        ...

class RoadStrategy(RouteStrategy):
    def build_route(self, origin: str, destination: str) -> List[str]:
        return [f"Sair de {origin}", "Pegar a rodovia BR-101", "Entrar na via local", f"Chegar em {destination}"]

class PublicTransportStrategy(RouteStrategy):
    def build_route(self, origin: str, destination: str) -> List[str]:
        return [f"Sair de {origin}", "Ônibus 345 até Estação Central", "Metrô Linha 2 até Final", f"Chegar em {destination}"]

class WalkingStrategy(RouteStrategy):
    def build_route(self, origin: str, destination: str) -> List[str]:
        return [f"Sair de {origin}", "Seguir 800m pela Rua das Flores", "Virar à esquerda na Praça", f"Chegar em {destination}"]
