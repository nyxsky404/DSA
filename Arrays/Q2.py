## Find the Second Largest in an Array

def getSecondLargest(self, arr):
    large = float('-inf')
    sec_large = float('-inf')
    
    for i in arr:
        if i > large:
            sec_large = large
            large = i
        elif i > sec_large and large != i:
            sec_large = i
    
    # For duplicates
    if sec_large == float('-inf'):
        return -1
    return sec_large


## Find the Second Smallest Element in an Array

def getSecondSmallest(self, arr):
    small = float('inf')
    sec_small = float('inf')

    for i in arr:
        if i < small:
            sec_small = i
            small = i
        elif i < sec_small and small != i:
            sec_small = i
    
    if sec_small == float('inf'):
        return -1
    return sec_small
