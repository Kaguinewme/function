def even(n):
    if n>10:
        i=0
        sum=0
        re=0
        while i<n:
            re=n%10
            sum=sum+re
            n=n//10
        return even(sum)
    else:
        if n%2==0:
            print(n,"even")
        else:
            print(n,"odd")
even(n=int(input("enter the number")))