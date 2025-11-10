#Find the third smallest element in an array:

def third_smallest(arr):
    arr = list(set(arr))  # remove duplicates
    arr.sort()
    if len(arr) < 3:
        return "Array doesn't have a third smallest element"
    return arr[2]

arr = [10, 4, 3, 50, 23, 90, 4]
print("Third smallest element:", third_smallest(arr))
