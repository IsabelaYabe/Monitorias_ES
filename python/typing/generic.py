print("============Generic Classes Simple Example============")
print("Inline Type Parameters")
def echo[T](value: T) -> T:
    return value
print("echo[T], echo(42): ", echo(42))        
class Box[T]:
    def __init__(self, item: T) -> None:
        self.item = item
    def get(self) -> T:
        return self.item

b1: Box[int] = Box(123)
b2: Box[str] = Box("oi")
x = b1.get()   # int
y = b2.get()   # str

print("b1.get(): ", x)
print("b2.get(): ", y)

print("============Generic Classes Convariant============")
from typing import Generic, TypeVar, reveal_type
T_co = TypeVar("T_co", covariant=True)  # leitura apenas → covariante

class ReadOnlyList(Generic[T_co]):
    def __init__(self, data: list[T_co]) -> None: 
        self._d = data

    def __getitem__(self, i: int) -> T_co: 
        return self._d[i]

def takes_objects(xs: ReadOnlyList[object]) -> object: 
    return xs[0]

rol_ex_1: ReadOnlyList[str] = ReadOnlyList(["a"])
rol_ex_2: ReadOnlyList[int] = ReadOnlyList([1, 2, 3])
takes_objects(rol_ex_1)  
takes_objects(rol_ex_2)

print("-----")
print(rol_ex_1[0])
print("-----")
print(rol_ex_2[0])
print("-----")

# print("============Reveal Type Tests============")
# reveal_type(rol_ex_1[0])
# reveal_type(rol_ex_2[0])
# 
# 
# from time import sleep
# sleep(0.7)  # Apenas para separar visualmente as seções

print("============Generic Classes Variant============")
from typing import TypeVar, Generic

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content

    def get_content(self) -> T:
        return self.content

box = Box(123)
print(box.get_content()) 

print("============Best Practices for Using TypeVar============")
from typing import TypeVar

Number = TypeVar('Number', int, float)

def add(a: Number, b: Number) -> Number:
    return a + b

print(add(1, 2))         # OK
print(add(1.5, 2.5))     # OK
print(add(1, 2.5))     # Type checker error