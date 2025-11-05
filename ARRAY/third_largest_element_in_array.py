#Find the third largest element in an array:

def third_largest(arr):
    arr = list(set(arr))  # remove duplicates
    arr.sort()
    if len(arr) < 3:
        return "Array doesn't have a third largest element"
    return arr[-3]

arr = [10, 20, 4, 45, 99, 45]
print("Third largest element:", third_largest(arr))
