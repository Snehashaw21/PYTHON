#Reverse an array with using  for loop:

def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
#array
arr = [10, 20, 30, 40, 50]

reversed_result = reverse_array(arr)
print("Reversed array:", reversed_result)
