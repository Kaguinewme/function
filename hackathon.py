
# def is_palindrome(a):
#     a=a.lower()
#     i=0
#     l=len(a)-1
#     if  a[i]==a[l]:
#         return True
#     else:
#         return False
# a="Abba"
# b=is_palindrome(a)
# if b:
#     print(True)
# else:
#     print(False)


 

a=[1,3,5,7,9,11,12,15]
def missing(a):
    b=[]
    i=1
    while i<=15:
       if i not in a:
          b.append(i)
       else:
          b.append(i)
       i+=1 
    return b
print(missing(a))


# def odd():
#     i=0
#     count=0
#     while i<7:
#         if i%2!=0:
#             count+=1
#         i+=1
#     return count
# print(odd())
            
            
