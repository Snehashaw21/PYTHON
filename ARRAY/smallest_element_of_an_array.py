#Find the smallest element in an array using a function:

def find_smallest(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

arr = [10, 45, 2, 99, 56]

result = find_smallest(arr)
print("The smallest element in the array is:", result)
