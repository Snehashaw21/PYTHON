#The Least Common Multiple (LCM) of two numbers:

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    return (a * b) // gcd

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm = find_lcm(a, b)
print(f"The LCM of {a} and {b} is: {lcm}")
