#Display the multiplication table of the given number

n=int(input("Enter the number: "))

print("Multiplication table of",n,"is:")

for i in range(1,11):
    print(n,"X",i,"=",n*i)
