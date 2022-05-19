list = [8, 6, 4, 8, 4, 50, 2, 7]
def min(list):
    i=0
    min=list[0]
    while i<len(list):
        if list[i]<min:
            min=list[i]
        i+=1
    return min
print(min(list))


