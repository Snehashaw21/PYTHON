#Print elements at even indexes of an array:

def elements(arr):
    for i in range(0, len(arr), 2):
        print(arr[i], end=" ")

n = int(input("Enter number of elements: "))
arr = [int(input("Enter element: ")) for _ in range(n)]

print("Elements at even indexes:")
elements(arr)
