# Selection Sort
#   Smallest elements first

nums = [5,7,8,4,1,6,9,2]


# Steps:
    # i from (0 to len(nums))
    # assume, min_idx = i
    # To check min_index, j from (i+1, len(nums))
    # if found nums[min_idx] > nums[j] : min_idx = j
    # nums[i],nums[min_idx] = nums[min_idx], nums[i]


for i in range(0,len(nums)):
    min_idx = i
    for j in range(i+1,len(nums)):
        if nums[min_idx] > nums[j]:
            min_idx = j
    nums[i],nums[min_idx] = nums[min_idx], nums[i]

print(nums)


# Time Complexity: O(N^2)
# Space Complexity: O(1)