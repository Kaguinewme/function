
def perfect(x):
    i=1
    while i<=1000:
       sum=0
       j=1
       while j<i:
           if i%j==0:
               sum=sum+j
           j+=1
       if sum==i:
           print(i,"is perfect no")
       i+=1
perfect(1000)