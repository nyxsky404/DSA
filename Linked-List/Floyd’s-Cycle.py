#* Question3 -> Leetcode 141: Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## BFS

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_set = set()
        curr = head
        while curr is not None:
            if curr not in my_set:
                my_set.add(curr)
                curr = curr.next
            else:
                return True
        return False

# Time Complexity: O(N)
# Space Complexity: O(N)

#! Note: Each Node is Unique due to there address but values of different node can be same 




## Optimized: Tortoise-Hare Approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
                    
# Time Complexity: O(N)
# Space Complexity: O(1)
