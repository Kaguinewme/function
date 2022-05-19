a = ['zero','one','two','three','four','five','six','seven','eight','nine',"ten"]
def word(n):
    if n!=0:
        x=a[n%10]
        return x
    else:
        pass
n=int(input("enter the number"))
print(word(n))
