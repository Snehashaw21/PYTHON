#Move all negative numbers to one side of the array:

def move_negatives(arr):
    negatives = [x for x in arr if x < 0]
    positives = [x for x in arr if x >= 0]
    return negatives + positives

arr = [1, -2, 3, -4, 5, -6, 7]
print("Rearranged Array:", move_negatives(arr))
