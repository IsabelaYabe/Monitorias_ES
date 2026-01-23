from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar

TState = TypeVar("TState")

@dataclass(frozen=True)
class Memento(Generic[TState]):
    state: TState
