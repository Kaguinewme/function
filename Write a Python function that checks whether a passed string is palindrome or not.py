
def palindrome(a):
    i=0
    j=len(a)-1
    while j>=i:
        if not a[i]==a[j]:
            return False
            i+=1
            j-=1
        else:
           return True
print(palindrome("mom"))
        
   
  