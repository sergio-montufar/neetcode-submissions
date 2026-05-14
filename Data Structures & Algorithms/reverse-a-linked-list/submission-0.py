# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_ptr, curr_ptr = None, head

        while curr_ptr:
            forward_ptr = curr_ptr.next
            curr_ptr.next = prev_ptr

            prev_ptr = curr_ptr
            curr_ptr = forward_ptr
            
        return prev_ptr
        