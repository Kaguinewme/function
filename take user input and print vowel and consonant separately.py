def count(a):
    vowel=0
    consonant=0
    i=0
    while i<len(a) :
        if a[i] in ("a","e","i","o","u"):
            print(a[i],"vowel")
        else:
            print(a[i],"consonant")
        i+=1
        
a=input("enter any character:")
count(a)