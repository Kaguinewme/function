
a= ['zero','one','two','three','four','five','six','seven','eight','nine']
def word(n):
    if(n==0):
        return ""
    else:
      x = a[n%10]
      y = word(int(n/10)) + x + " "
    return  y
n = int(input("enter the number:"))
print(word(n))