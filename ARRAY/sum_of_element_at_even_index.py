#Find the sum of elements at even indexes:

def sum_even_index(arr):
    total = 0
    for i in range(0, len(arr), 2):  # step = 2 → even indexes only
        total += arr[i]
    return total

# Example
arr = [10, 20, 30, 40, 50, 60]
print("Array:", arr)
print("Sum of elements at even indexes:", sum_even_index(arr))
