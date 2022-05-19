list =(8, 2, 3, 8, 7,4,5,6,7)
def add(list):
    i=0
    count=0
    while i<len(list):
        count=count+1
        i+=1
    return count
print(add(list))