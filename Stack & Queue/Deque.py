# To convert O(N) to O(1) in enqueue/ dequeue in Queues, we use deque


from collections import deque

lst = deque([])

# enqueue
lst.append(6) # adding at end
lst.append(9)

lst.appendleft(7) # adding at first
lst.appendleft(5)


# dequeue
lst.pop() # removing from end
lst.popleft() # removing from first

print(lst)



# Size
print(len(lst))

# front & rear
print(lst[0])
print(lst[-1])



