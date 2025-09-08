#Find the third largest element in an array:

def third_largest(arr):
    arr = list(set(arr))  # remove duplicates
    if len(arr) < 3:
        return "Array does not have 3 distinct elements"
    arr.sort()
    return arr[-3]

arr = [10, 20, 4, 45, 99, 45, 33]
print("Array:", arr)
print("Third largest element:", third_largest(arr))
