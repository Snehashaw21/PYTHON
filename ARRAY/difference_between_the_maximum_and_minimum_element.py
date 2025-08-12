#Find the difference between the maximum and minimum element in an array:

def differ_max_min(arr):
    return max(arr) - min(arr)

# Taking input
n = int(input("Enter number of elements: "))
arr = [int(input("Enter element: ")) for _ in range(n)]

print("Difference between max and min element:", differ_max_min(arr))
