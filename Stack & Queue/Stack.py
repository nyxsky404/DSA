# What is Stack? : Can store any type of Date.
# What mechanism is used?: LIFO[Last in First Out]

# Operations:
#   push(x)
#   pop()
#   top()
#   Size()


## IMPLEMENT STACK USING ARRAY/LIST
#   push(x) -> .append(x)
#   pop() -> .pop()
#   top() -> arr[-1]
#   Size() -> len(arr)

#! These operations in python has time complexity: O(1)

class Stack:
    def __init__(self):
        self.items = []

    def push(self,val):
        self.items.append(val)
    
    def pop(self):
        if len(self.items) == 0:
            return ("empty stack")
        return self.items.pop()
    
    def top(self):
        if len(self.items) == 0:
            return ("empty stack")
        return self.items[-1]

    def size(self):
        if len(self.items) == 0:
            return ("empty stack")
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0


s = Stack()
s.push(5)
s.push(10)
s.push(15)
print(Stack)
print(s.pop())
print(Stack)
print(s.pop())
print(s.top())
print(s.size())
print(s.is_empty())