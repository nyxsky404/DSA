#* Question4-> GFG: Find length of Loop

## Optimized: Tortoise-Hare Approach

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                fast = fast.next   
                count = 1
                while slow != fast:
                    fast = fast.next
                    count += 1
                return count
        return 0

# Time Complexity: O(N)
# Space Complexity: O(1)