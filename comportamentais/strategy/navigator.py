from route_strategy import RouteStrategy, RoadStrategy, WalkingStrategy, PublicTransportStrategy
from typing import List

class Navigator:
    def __init__(self, strategy: RouteStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: RouteStrategy) -> None:
        self._strategy = strategy

    def build_route(self, origin: str, destination: str) -> List[str]:
        return self._strategy.build_route(origin, destination)

if __name__ == "__main__":
    nav = Navigator(WalkingStrategy())
    print("A pé:", nav.build_route("Ponto A", "Ponto B"))

    nav.set_strategy(RoadStrategy())
    print("De carro:", nav.build_route("Ponto A", "Ponto B"))

    nav.set_strategy(PublicTransportStrategy())
    print("Transporte público:", nav.build_route("Ponto A", "Ponto B"))