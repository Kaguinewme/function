a=[1,2,3],[4,5,6],[7,8,9]
def list(a):
    i=0
    b=[]
    while i<len(a):
        j=0
        while j<len(a[i]):
            print(a[i][j],end=" ")
            j+=1
        i+=1
list(a)
