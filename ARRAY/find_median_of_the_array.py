#Find the median of the array:

def find_median(arr):
    arr.sort()  
    n = len(arr)
    
    if n % 2 == 1:  
        return arr[n // 2]
    else:           
        mid1 = arr[n // 2 - 1]
        mid2 = arr[n // 2]
        return (mid1 + mid2) / 2

arr = [7, 1, 3, 5, 9]
print("Median:", find_median(arr))
