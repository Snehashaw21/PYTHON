#Remove duplicates from an array:

def remove_duplicates(arr):
    unique = []
    for item in arr:
        if item not in unique:
            unique.append(item)
    return unique

arr = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(arr)
print("Array after removing duplicates:", result)
