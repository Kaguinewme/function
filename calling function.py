def add(x):
    return x+1
def add_one(add,x):
    return add(x)*2
print(add_one(add,7))


##calling function operator
def add(a,b):
    c=a+b
    return c

def pro(a,b):
    d=a*b
    return d 

def div(a,b):
    c=a/b 
    return c
def sub(a,b):
    c=a-b
    return c
def main():
    print(add(5,7))
    print(pro(7,8))
    print(div(4,2))
    print(sub(8,2))
main()


 
