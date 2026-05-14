# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr





        # if root == q:
        #     return q
        # if root == p:
        #     return p

        # if root.val >= p.val and root.val <= q.val:
        #     return root
            
        
        # if root.val >= p.val and root.val >= q.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif root.val <= p.val and root.val <= q.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        

        