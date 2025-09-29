#Find the majority element (element that appears more than n/2 times):

def element(arr): 
    n = len(arr)
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > n // 2:
            return num   
    return None  

arr = [3, 3, 4, 2, 3, 3, 5, 3]
print("Majority Element:", element(arr)) 
