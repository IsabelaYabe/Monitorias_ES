def multiplier(fator):
    def apply(x: int) -> int:
        return fator * x
    return apply

x2 = multiplier(2)
# print(x2)
print(x2(5))
