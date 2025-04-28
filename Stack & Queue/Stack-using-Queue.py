## Implement Stack using Queue/deque

#! Stacks last/top element must be first element of queue

# Operations:
#  push:
    #  append
    #  rotate whole list by (len-1)

#   pop: remove first element (0 th)
#   top: first element
#   size : length 


from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.items = deque([])
    
    def push(self,val):
        self.items.append(val)

        #! Rotating array
        for i in range(len(self.items) - 1):
            self.items.append(self.items.popleft())

    
    def pop(self):
        if len(self.items) == 0:
            return ("empty stack")
        return self.items.popleft()
    
    def top(self):
        if len(self.items) == 0:
            return ("empty stack")
        return self.items[0]
    
    def size(self):
        return len(self.items)
    