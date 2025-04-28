## Find the maximum Element in an Array

def maximum(arr):
    max = float('-inf')
    for i in arr:
        if i > max:
            max = i
    
    return max

## Find the minimum Element in an Array

def minimum(arr):
    min = float('+inf')
    for i in arr:
        if i < min:
            min = i
    
    return min