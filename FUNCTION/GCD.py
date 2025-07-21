#Find the Greatest Common Divisor (GCD) of two numbers.

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"The GCD of {x} and {y} is: {find_gcd(x, y)}")
