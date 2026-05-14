# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_ptr, fast_ptr = head, head.next

        # this loop is to have the slow_ptr go into the middle of the list
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        
        second = slow_ptr.next
        prev = slow_ptr.next = None

        # this is to reverse the 2nd half of the linked list
        # 1 --> 2 --> 3 | None <-- 1 <-- 2 <-- 3
        while second:
            temp = second.next
            second.next = prev
            prev = second

            second = temp
        
        first, second = head, prev
        # first = 2
        # second = 8

        # start: 2 --> 4 --> 8 --> 6
        #   end: 2 --> 8 --> 4 --> 6  
        
        # | 2 --> 8 |  8 --> 4 | 4 --> 6
        while second:
            # temp_1 = 4
            # temp_2 = 6
            temp_1, temp_2 = first.next, second.next 
            first.next = second # 2 --> 8 (first iter)
            second.next = temp_1 # 8 --> 4 (first iter)
            first, second = temp_1, temp_2

            # second iter:
            # first, second = 4, 6
            # temp_1, temp_2 = 
            
    





