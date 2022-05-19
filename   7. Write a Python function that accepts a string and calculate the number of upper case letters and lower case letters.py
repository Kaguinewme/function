
def string(s):
    lower=0
    upper=0
    for i in s:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
    print("original string",s)
    print("no of lower case", lower)
    print("no of upper case",upper)
string("The Quick Brown FOx")
  

