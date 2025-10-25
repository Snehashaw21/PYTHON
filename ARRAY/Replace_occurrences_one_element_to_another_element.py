#Replace all occurrences of a given element with another element:

def replace_all(arr, old, new):
    for i in range(len(arr)):
        if arr[i] == old:
            arr[i] = new
    return arr 

arr = [10, 20, 30, 20, 40, 20, 50]
print("Original array:", arr)

arr = replace_all(arr, 20, 99)
print("After replacement:", arr)
