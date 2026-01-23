from dataclasses import dataclass

@dataclass(frozen=True)
class Memento:
    content: str
    font: str
    font_size: int
