#Print all elements that are greater than the average value:

def average(arr): 
    avg = sum(arr) / len(arr)
    print("Average value:", avg) 
    print("Elements greater than average:")
    for num in arr:
        if num > avg:
            print(num, end=" ")

arr = [10, 20, 30, 40, 50]
average(arr)
