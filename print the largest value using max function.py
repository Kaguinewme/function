
numbers=[3,5,7,34,2,89,2,5,90]
def maximum(numbers):
    i=0
    max=numbers[0]
    while i<len(numbers):
        if numbers[i]>max:
            max=numbers[i]
        i+=1
    return max
print(maximum(numbers))

        
    