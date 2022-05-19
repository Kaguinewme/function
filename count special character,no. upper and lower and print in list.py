s="123@#KaguiNEWME"
def string(s):
    lower=0
    upper=0
    number=0
    ch=0
    c=[]
    for i in s:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
        elif i.isdigit():
            number+=1
        else:
            ch+=1
    c.append(lower)
    c.append(upper)
    c.append(number)
    c.append(ch)
    print(c)
string(s)