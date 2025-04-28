# Merge Sort
    # Divide & conquer/merge technique

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    l_half = arr[:mid]
    r_half = arr[mid:]
    l_half = merge_sort(l_half)
    r_half = merge_sort(r_half)
    return merge(l_half, r_half)

def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    #Add remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    #* if extend not working
    # while i < len(left):
    #     merged.append(left[i])
    #     i += 1

    # while j < len(right):
    #     merged.append(right[j])
    #     j += 1

    return merged