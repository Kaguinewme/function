##9. Write a Python function that takes a number as a parameter and check the number is prime or not. Go to the editor
##Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(3))