#Print Fibonacci sequence 

n = int(input("How many fibonacci number you want: "))
a = 0
b = 1

print("Fibonacci sequence:")
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
