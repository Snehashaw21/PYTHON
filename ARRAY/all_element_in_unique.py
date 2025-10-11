#Check if all elements in an array are unique(True&False):
#OUTPUT:
#Array 1 Unique: True
#Array 2 Unique: False



def all_unique(arr):
    return len(arr) == len(set(arr))

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 2, 5]

print("Array 1 Unique:", all_unique(arr1))
print("Array 2 Unique:", all_unique(arr2))
