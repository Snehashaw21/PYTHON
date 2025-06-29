#find the factorial of the given number....

num = int(input("Enter the number: "))
fact = 1

if (num < 0):
    print("Factorial doesn't exist for negative numbers.")
elif (num == 0):
    print("Factorial of the number is 1")
else:
    for i in range(1, num + 1):
        fact =fact * i
    print("Factorial of the number is", fact)
