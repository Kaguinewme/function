list=[-50,-3,-1,-2,-4,-6]
i=0
max=0
sec=0
def secmax():
    if list[i]>max :
        max=list[i]
    if list[i]>sec:
        sec=list[i] 
    return sec
    i+=1
list.sort()
print(list[-2])