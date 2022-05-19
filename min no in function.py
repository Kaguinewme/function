a=[-50,-3,-1,-2,-4,-6]
i=0
while i<len(a):
    j=0
    while j<(len(a)):
        if a[i]<a[j]:
             b=a[i]
             a[i]==a[j]
             a[j]=b
        j+=1
    i+=1
print(b)

        