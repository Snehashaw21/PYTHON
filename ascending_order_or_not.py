#Check if the array elements are in ascending order:

def is_ascending(arr):
    return arr == sorted(arr)

arr = [10, 20, 30, 40]
print("Is ascending:", is_ascending(arr))
