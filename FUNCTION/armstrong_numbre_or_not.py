#Usin function Check the number is armstrong or not: 

def is_armstrong(number):
    num_str = str(number)
    num_length = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
    
    if sum_of_powers == number:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
