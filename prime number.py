def add():
    a=[1,2,3,4,5,6,7,8,9,10,11]
    i=1
    b=[]
    while i<len(a):
        if a[i]%2!=0 or a[i]==2 :
            b.append(a[i])
        i=i+1
    print("prime no",b)   
add ()

   