list=[1,2,3,4,5,6]
def reverse(list):
    i=-1
    a=[]
    while i>=-len(list):
        a.append(list[i])
        i=i-1
    return a
print(reverse(list))