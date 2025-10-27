#Separate even and odd numbers into two different arrays: 

def separate_even_odd(arr):
    even = []
    odd = []
    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

arr = [10, 21, 4, 45, 66, 93, 22]
even, odd = separate_even_odd(arr)

print("Original array:", arr)
print("Even numbers:", even)
print("Odd numbers:", odd)
