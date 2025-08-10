Find the intersection of two array:

def intersection(arr1, arr2):
    result = []
    for item in arr1:
        if item in arr2 and item not in result:
            result.append(item)
    return result

# Example arrays
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]

print("Intersection:", intersection(arr1, arr2))
