#Check the number is prime or not using for loop

num = int(input("Enter the number: "))

for i in range(2,num):
    if (num%i)==0:
        print("It is not a prime number.")
        break
else:
    print("The number is prime.")
