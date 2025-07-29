#Find the largest element in an array:



def find_largest(arr):
    if not arr:
        return None
    
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

array = [12, 45, 2, 67, 33, 89, 23]
print("The largest element is:", find_largest(array))
