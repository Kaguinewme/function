def add(a,b):
    i=1
    sum=0
    while i<=b:
        if i%a==0:
            sum=sum+i
        i+=1
    return sum
a=int(input("enter the first number"))
b=int(input("enter the second number"))
print(add(a,b)) 