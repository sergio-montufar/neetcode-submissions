# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 6 --> 2 --> 4
        # 3 --> 1 --> 7
        # 9 --> 3 --> 1 --> 1 (sum is in reverse)

        # 0 --> 0 --> 9
        # 0 --> 0 --> 2 --> 1
        # 0 --> 0 --> 1 --> 2


        # 9 --> 9 --> 9
        # 9 --> 9 --> 9
        # 8 --> 9 --> 9 --> 1



        carry = 0
        ans_node = ListNode()
        curr = ans_node
        while l1 or l2 or carry:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            
            add = l1.val + l2.val + carry
            carry = add // 10
            add = add % 10
            curr.next = ListNode(add)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return ans_node.next
