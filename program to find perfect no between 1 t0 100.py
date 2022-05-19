
num1=int(input("enter the first number "))
num2=int(input("enter the sec number"))
for i in range (num1,num2):
    sum=0
    for j in range(1,i):
        if (i%j==0):
            sum=sum+j
    if (sum==i):
        print(i)

            
    
