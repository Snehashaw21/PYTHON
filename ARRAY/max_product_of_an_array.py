#Find the maximum product of two elements in an array:

def max_product(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return first * second

arr = [5, 20, 2, 6, 18, 9]
print("Array:", arr)
print("Maximum product of two elements:", max_product(arr))
