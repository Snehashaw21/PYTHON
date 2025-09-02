#Find the sum of elements at odd indexes:

def sum_odd_index(arr):
    total = 0
    for i in range(1, len(arr), 2): 
        total += arr[i]
    return total

arr = [10, 20, 30, 40, 50, 60]
print("Array:", arr)
print("Sum of elements at odd indexes:", sum_odd_index(arr))
