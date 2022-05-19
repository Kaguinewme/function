list1=[2,6,18,10,3,75]
list2=[6,19,24,12,3,87]
def check_number(list1,list2):
    i=0
    j=0
    while i<len(list1) and j<len(list2):
        if list1[i]%2==0 and list2[j]%2==0:
            print("both even")
        else:
            print("both are not even")
        i+=1
        j+=1
check_number(list1, list2)


            