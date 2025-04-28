# FIFO[First in First Out]

# Operations:
#   enqueue(x) : add element to queue (at last)
#   dequeue() : remove first element
#   front(): first element
#   rear(): last element
#   Size()
#   is_empty()


## IMPLEMENT Queue USING ARRAY/LIST

#! if inserting at end and removing from first in array
#   enqueue(x) -> .append(x)
#   dequeue() -> .pop(0)
#   front() -> arr[0]
#   rear() -> arr[-1]
#   Size() -> len(arr)
#   is_empty() -> len(arr) == 0
#! only dequeue takes O(N) and all other operations has O(1)

class Queue:
    def __init__(self):
        self.items =[]
    
    def enqueue(self,val):
        self.items.append(val)

    def dequeue(self):
        if len(self.items) == 0:
            return ("empty queue")
        return self.items.pop(0)
    
    def front(self):
        if len(self.items) == 0:
            return ("empty queue")
        return self.items[0]
    
    def rear(self):
        if len(self.items) == 0:
            return (" Queue Empty")
        return self.items[-1]
    
    def Size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0



Q = Queue()

Q.enqueue(5)
Q.enqueue(10)
Q.enqueue(56)
Q.enqueue(64)
print(Q.Size())
print(Q.front())
print(Q.rear())
print(Q.dequeue())
print(Q.dequeue())
print(Q.front())
print(Q.rear())
print(Q.is_empty())



#! if inserting at beginning and removing from end in array
#   enqueue(x) -> .insert(0,x)
#   dequeue() -> .pop()
#   front() -> arr[0]
#   rear() -> arr[-1]
#   Size() -> len(arr)
#   is_empty() -> len(arr) == 0

#! only enqueue takes O(N) and all other operations has O(1)