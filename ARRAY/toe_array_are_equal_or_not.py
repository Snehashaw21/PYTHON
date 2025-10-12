#Check if two arrays are equal (same elements in any order):
#OUTPUT:
#a & b equal: True
#a & c equal: False


def arrays_equal(arr1, arr2):
    return sorted(arr1) == sorted(arr2)

a = [1, 2, 3, 4]
b = [4, 3, 2, 1]
c = [1, 2, 2, 3]

print("a & b equal:", arrays_equal(a, b))
print("a & c equal:", arrays_equal(a, c))
