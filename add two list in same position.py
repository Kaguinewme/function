list1=[50,60,10]
list2=[10,20,13]
def add_two_list(list1,list2):
    i=0
    j=0
    add=0
    while i<len(list1) and j<len(list2):
        add=list1[i]+list2[j]
        print(add)
        i+=1
        j+=1
add_two_list(list1, list2)          