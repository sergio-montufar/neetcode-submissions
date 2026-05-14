# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2

        temp_head = ans = ListNode()

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                ans.next = ptr1
                ptr1 = ptr1.next
            else:
                ans.next = ptr2
                ptr2 = ptr2.next

            ans = ans.next
        ans.next = ptr1 or ptr2

        return temp_head.next
        