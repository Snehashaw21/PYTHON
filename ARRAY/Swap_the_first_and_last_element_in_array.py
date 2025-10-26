#Swap the first and last element of an array.

def swap_first_last(arr):
    if len(arr) > 1:   # Check array has at least 2 elements
        arr[0], arr[-1] = arr[-1], arr[0]
    return arr

arr = [10, 20, 30, 40, 50] 
print("Original array:", arr)
print("After swapping:", swap_first_last(arr))
