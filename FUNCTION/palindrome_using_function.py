#Check the number is palindrome or not using function:

def is_palindrome(n):
    rev = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    return n == rev

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
     print(f"{num} is not a palindrome number.")
