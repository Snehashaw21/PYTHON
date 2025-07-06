#check the prime number in between 1-50:
#2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print("Prime numbers between 1 and 50 are:")
for num in range(1, 51):
    if is_prime(num):
        print(num, end=' ')
