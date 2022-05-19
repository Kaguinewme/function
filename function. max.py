list=[5,6,7,8,11,34,56,80,67]
def max(list):
    i=0
    max=list[0]
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i+=1
    return max
print(max(list))



