#* Question4-> Leetcode 142: Linked List Cycle II

## BFS
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_set = set()
        curr = head

        while curr is not None:
            if curr in my_set:
                return curr
            my_set.add(curr)
            curr = curr.next
        
        return None
    
# Time Complexity: O(N)
# Space Complexity: O(N)

#! Note: "null" is "None" in python


## Optimized: Tortoise-Hare Approach
#! Re-watch the prof

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

# Time Complexity: O(N)
# Space Complexity: O(1)