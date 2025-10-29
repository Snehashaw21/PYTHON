#Print all elements that are greater than the average value:

def greate(arr):
    avg = sum(arr) / len(arr)
    print("Average value:", avg)
    print("Elements greater than average:")
    for num in arr:
        if num > avg:
            print(num, end=" ")


arr = [5, 10, 15, 20, 25]
greater(arr)
