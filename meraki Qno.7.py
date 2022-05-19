#Define a function which takes two arguments(strings) and returns the string with largest
#length. If both the strings have equal length, print both the strings one below the other.
##Hint :- use len() builtin function.
##Hint :- use len() builtin function..
 
##function_name(“hello”,”welcome”)
##function_name(“sonu”,”monu”)


def name(a,b,c,d ):
    if len(a)> len(b) and len(a)>c and len(a)>len(d):
        print(a)
    if  len(b)>len(a) and len (b)> len(c) and len(b)> len(d):
        print(b)
    if len(c)>len(a) and  len(c)>len(b) and len(c)>len(d):
        print(c)
    if len(d)>len(a) and len(d)>len(b) and len(d)>len(c):
        print(d)
    if len(a)==len(b):
        print(a)
        print(b)
    if len (c)==len(d):
        print(c)
        print(d)
name("hello","welcome","sonu","monu")
        
    
    



         

