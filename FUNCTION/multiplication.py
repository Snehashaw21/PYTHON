#Multplication:

def multiplication_table(n):
    print(f"Multiplication Table of {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number : "))

multiplication_table(num)
