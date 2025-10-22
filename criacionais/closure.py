# Local, Enclosing, Global, Built-in 

var = "global"

def funcao0():
    var = 10
    print(var)

def funcao1():
    var = 2
    def interna():
        # var = 1
        print(var)
    interna()

# print(var)
# funcao0()
funcao1()