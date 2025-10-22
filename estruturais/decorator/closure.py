def multiplier(fator):
    def apply(x: int) -> int:
        return fator * x
    return apply

x2 = multiplier(2)
print(x2)
x2 = multiplier(2)
print(x2(5))

def main():
    def multiplier(fator):
        def apply(x: int) -> int:
            return fator * x
        return apply


    x2 = multiplier(2)
    print(x2)
    # x2 = multiplier(2)
    # print(x2(5))
    return x2

x2 = main()
print(x2)

class Classe():
    def __init__(self, x):
        self.x = x

classe = Classe(2)

print(classe)