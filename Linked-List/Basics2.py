class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Singly:
    def __init__(self):
        self.head = None 
    
    def append(self,val):
        new_node = Node(val)

        # Case1: SLL is empty: head = none
        if self.head == None:
            self.head = new_node
        
        # Case2: SLL is not empty: Traverse until find None
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    
    def traverse(self):
        # Case1: SLL is empty
        if self.head is None:
            print("SLL is empty")
        else:
            curr = self.head
            while curr is not None: #Note: using curr.next, stops before the last node as loop ends when curr.next is None.
                print(curr.val, end="")
                curr = curr.next
            print()
    
    def insert_at_position(self, val, position):
        new_node = Node(val)

        # insert at beginning
        if position == 0:
            new_node.next = self.head
            self.head = new_node

        # insert at in b/w
        else:
            curr = self.head
            prev = None
            count = 0
            while curr is not None and count < position:
                prev = curr
                curr = curr.next
                count +=1
            prev.next = new_node
            new_node.next = curr
    
    def delete(self,val):
        temp = self.head

        # delete first note if only one node is present
        if temp.next is None:
            self.head = None

        # delete first node if it has next nodes
        if temp.next is not None:
            self.head = self.head.next
        
        # if given value's Node, we have to delete
        curr = self.head
        if curr.next is not None: # checking if empty SLL
            if curr.val == val:
                self.head = self.head.next
                return
            else:
                found = False
                prev = None
                while curr is not None:
                    if curr.val == val:
                        found = True
                        break
                    prev = curr
                    curr = curr.next

                if found:
                    prev.next = curr.next
                    return
                else:
                    print("Node not found")

    def removeNthFromStart(self,n):
        # n is position that we have to delete
        
        prev = None
        curr = self.head

        # if empty
        if curr is None:
            return None
        
        # first element
        elif n == 1:
            curr = self.head
            if curr.next is not None:
                self.head = curr.next
            else:
                self.head = None

        # nth and last element
        elif curr is not None:
            for i in range(1,n):
                prev = curr
                curr = curr.next
            
            if curr.next is not None:
                prev.next = curr.next
            else:
                prev.next = None
        
        return self.head


SL = Singly()
SL.append(5)