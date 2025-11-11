from typing import Protocol, runtime_checkable

@runtime_checkable
class Flyer(Protocol):
    def fly(self) -> None: ...

class Bird:
    def fly(self) -> None:
        print("flap")

class Rock:
    pass

b = Bird()
r = Rock()

print(isinstance(b, Flyer))  # True  (tem método fly)
print(isinstance(r, Flyer))  # False (não tem fly)
