#Find the minimum positive number in an array:

def positive(arr):
    positives = [num for num in arr if num > 0]
    if positives:
        return min(positives)
    else:
        return "No positive numbers found"

arr = [-5, 0, 3, -2, 7, 1, -8]
print("Minimum positive number:", positive(arr))
