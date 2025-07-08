#FIBONACCI SEQUENCE:
#0 1 1 2 3 5 8 13 21 34

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n_terms = 10
print("Fibonacci sequence:")
for i in range(n_terms):
    print(fibonacci(i), end=" ")
