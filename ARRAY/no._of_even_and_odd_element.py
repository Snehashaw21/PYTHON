Count the number of even and odd elements in an array:

def count_even_odd(arr):
    even = 0
    odd = 0
    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

arr = [1, 2, 3, 4, 5, 6, 7, 8]

even_count, odd_count = count_even_odd(arr)
print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)
