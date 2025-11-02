#Find the second smallest element in an array:

def second_smallest(arr):
    arr = list(set(arr))  
    arr.sort()
    if len(arr) < 2:
        return "Array doesn't have a second smallest element"
    return arr[1]

arr = [5, 1, 8, 3, 2, 1]
print("Second smallest element:", second_smallest(arr))
