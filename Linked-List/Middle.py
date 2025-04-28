#Question1 -> Leetcode-876: Middle of the Linked List

## BFS

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        curr = head
        while curr is not None:
            len +=1
            curr = curr.next
        
        curr = head

        for i in range(0,len//2):
            curr = curr.next
        
        return curr


## Tortoise-Hare Approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast != None or fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    

# Time Complexity: O(N/2)
# Space Complexity: O(1)