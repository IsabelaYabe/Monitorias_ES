from abc import abstractmethod
from typing import ClassVar, Protocol

class ProtocolMembersDemo(Protocol):
    class_attribute: ClassVar[int]
    instance_attribute: str = ""

    def instance_method(self, arg1: int, arg2: str) -> None:
        ...

    @classmethod
    def class_method(cls) -> str:
        ...

    @staticmethod
    def static_method() -> int:
        ...

    @property
    def property_name(self) -> bool:
        ...

    @property_name.setter
    def property_name(self, value: bool) -> None:
        ...

    @abstractmethod
    def abstract_method(self) -> str:
        ...
