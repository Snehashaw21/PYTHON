#Factorial is the basic example of recursion
#Finding the factorial of given number

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n=int(input("Enter the number:"))
print(f"Factorial of {n} is :{factorial(n)}")
