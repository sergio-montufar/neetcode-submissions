# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

       
        node_to_delete = length - n
        if node_to_delete == 0:
            return head.next
            
        curr = head
        i = 0
        while curr:
            if i+1 == node_to_delete:
                curr.next = curr.next.next
            i += 1
            curr = curr.next

        return head
