a=int(input("enter the  first number:"))
b=int(input("enter the  second number:"))
n=input("enter the operator:")
def add():
    add=a+b
    return add

def sub():
    sub=a-b
    return sub

def mul():
    mul=a*b
    return mul

def div():
    div=a/b
    return div

def main_fun():
    if n=='add':
        print(add())
    if n=='sub': 
        print(sub())
    if n=='mul':
        print(mul())
    if n=='div':
        print(div())
main_fun()



        
        
        
