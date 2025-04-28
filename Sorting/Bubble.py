# Bubble Sort (Adjacent swap: aaju- baaju)
#   Just like bubble comes above, the largest elements goes to last


# Steps:
    # Move i from last 2nd element to first element (range(len(nums)-2,-1,-1))
    # Move j from 0th to "i"th element
    # Check if nums[j] > nums[j+1], and swap them
    # if swap doesn't happen in first iteration: it means it's already sorted


nums = [5,7,8,4,1,6,9,2]

for i in range(len(nums)-2,-1,-1):
    Swapped = False
    for j in range(0,i+1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1],nums[j]
            Swapped = True
    if Swapped == False:
        break

print(nums)
    

# Time Complexity: O(N^2)
# Space Complexity: O(1)