#Find the union of two arrays:

def union_arrays(arr1, arr2):
    result = arr1[:]  # copy first array
    for item in arr2:
        if item not in result:
            result.append(item)
    return result

arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]

print("Union:", union_arrays(arr1, arr2))
