from datetime import date

class Calculator:
    def __init__(self, version: int):
        self.version = version

    # instance_method
    def description(self):
        print(f"Description: {self.version}")

    @staticmethod
    def add_numbers(*numbers: float) -> float:
        return sum(numbers)

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def description(self) -> str:
        return f"{self.name} is {self.age} years old"

    @classmethod
    def age_from_year(cls, name: str, birth_year: int) -> self:
        current_year: int = date.today().year
        age: int = current_year - birth_year
        return cls(name, age)


def main():
    calc_1 = Calculator(10)
    calc_2 = Calculator(20)

    calc_1.description()
    calc_2.description()

    print(Calculator.add_numbers(10,20,30))

    bela = Person.age_from_year("Bela", 1999)
    print(bela.description)

if __name__ == "__main__":
    main()