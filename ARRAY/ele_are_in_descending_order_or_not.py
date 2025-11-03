#Check if the array elements are in descending order or not:

def is_descending(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False
    return True

arr1 = [9, 7, 5, 3, 1]
arr2 = [10, 20, 15, 5] 

print("Array 1 descending:", is_descending(arr1))
print("Array 2 descending:", is_descending(arr2))
