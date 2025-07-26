#Find the largest and smallest element in an array (list):

arr = [10, 25, 8, 56, 3]

largest = arr[0]
smallest = arr[0]

for num in arr:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number is:", largest)
print("Smallest number is:", smallest)
