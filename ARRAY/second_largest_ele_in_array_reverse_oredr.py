#Find the second largest element in an array (reverse):

def second_largest(arr):
    arr = list(set(arr))  # remove duplicates
    arr.sort()
    if len(arr) < 2:
        return "Array doesn't have a second largest element"
    return arr[-2]

arr = [10, 20, 4, 45, 99, 45]
print("Second largest element:", second_largest(arr))
