#Swap alternate elements in the array:

def swap_alternate(arr):
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

arr = [1, 2, 3, 4, 5, 6]
print("Original array:", [1, 2, 3, 4, 5, 6])
print("After swapping alternate elements:", swap_alternate(arr))
