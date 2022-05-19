question=["How many continents are there?", "What is the capital of India?", "Which course is taught in navgurukul?"]
option=[["Four", "Nine","six", "Seven"],["Bihar", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
answer=[4,4,1]
def a(kbc):
    i=0
    while i<len(option[kbc]):
        print(i+1,option[kbc][i])
        i=i+1
    user= int(input('enter your answer'))
    if user==answer[kbc]:
        return True
    else:
        return False
def b():
    j=0
    while j<len(question):
        print(j+1,question[j])
        result=a(j)
        if result==True:
            print("congratulations!! your answer is correct")
        else:
            print("your answer is wrong")
            break   
        j=j+1

def main():
    b()
main()
 


        