#Check if the array elements are in ascending order:

def is_ascending(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 3, 4, 2]

print("Array 1 ascending:", is_ascending(arr1))
print("Array 2 ascending:", is_ascending(arr2))
