n=10
def funct1():
    print(n)
def funct2():
    n=20
    print(n)
    funct1()
funct2()
    