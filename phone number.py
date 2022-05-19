def add():
    a=([1,2,3,0,5,6,0,8,9,])
    b=""
    c=""
    d="-"
    i=0
    while i<len(a):
        if i<3:
            b=b+str(a[i])
        if i>=3 and i<=5:
            c=c+str(a[i])
        if i>=6:
            d=d+str(a[i])
        i=i+1
    y="("+b+")"
    print(y+c+d)
add()