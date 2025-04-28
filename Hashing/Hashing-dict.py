nums = list(map(int,input().split(" ")))

## Method 1
freq = {}

for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

# Time Complexity: O(N)
# Space Complexity: O(N)


## Method 2
hash_map = {}

for i in nums:
    hash_map[i] = hash_map.get(i,0) + 1

print(hash_map)

# Time Complexity: O(N)
# Space Complexity: O(N)