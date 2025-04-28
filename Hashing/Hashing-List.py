# Hashing using List

#! Limitation: if constraint allows, then we can use it. else, use dictionary

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

# Constraints
# 1<=n[i]<=10
# n can have 10^8 elements
# m can have 10^8 elements

hash_list = [0] * 11   #constraint 1
for i in n:
    hash_list[i] += 1

for i in m:
    if 1<=i<=10:
        print(hash_list[i])
    else:
        print(0)
