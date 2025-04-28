## Edge Case:

#    1. Empty list
#    2. 0, +ve ,-ve elements
#    3. Duplicate elements


## Remember: whenever comparing "i" with "i+1", make the loop range accordingly.
    # range(0,len(arr)) : wrong (Error: index out of range)
    # range(0, len(arr)-1) : correct

## Infinity in python
    # positive = float('inf')
    # negative = float('-inf')