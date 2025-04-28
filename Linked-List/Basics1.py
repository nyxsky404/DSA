class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# CREATING NODES: Providing the Data, and "next" will be None
node1 = Node(1) 
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

print(node1) #gives address
print(node2.val) # gives value
print(node1.next) # gives address of next/ None

# CREATING LINKED LIST: giving address, node4 will have none
node1.next = node2
node2.next = node3
node3.next = node4

print(node1.next) 
print(node2) # ykyk: node1.next address same as node2 address
print(node1.next.val) # gives value of next
print(node1.next.next.next) 
print(node1.next.next.next.val)  