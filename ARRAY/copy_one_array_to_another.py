#Copy one array into another (without using slicing):

def copy_array(arr):
    new_arr = []
    for i in arr:
        new_arr.append(i)
    return new_arr

arr1 = [10, 20, 30, 40, 50]
arr2 = copy_array(arr1)

print("Original array:", arr1)
print("Copied array:", arr2)
