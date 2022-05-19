##Define a function that checks the speed of drivers. This function will take a
# parameter named speed, and will satisfy the following conditions:
##1.If speed if less than 70, print 70.
##2.If speed is more than 70, give 1 point per 5km.(NOTE:This won't count 70).
##3.If points are more than 12, print “License suspended”

def a(speed):
    c=(speed-71)//5+1
    if speed<=70:
        print("70")
    elif c>12:
        print("license suspended") 
    elif speed>70:
        print(c)
speed=int(input("enter the speed"))
a(speed)
