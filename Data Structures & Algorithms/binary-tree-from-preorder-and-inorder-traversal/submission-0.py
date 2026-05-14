# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {num: i for i, num in enumerate(inorder)}
        
        self.index = 0

        def dfs(left, right):
            if left > right:
                return None
            root_val = preorder[self.index]
            self.index += 1
            root = TreeNode(root_val)
            middle = hashmap[root_val]
            root.left = dfs(left, middle - 1)
            root.right = dfs(middle + 1, right)
            
            return root


        return dfs(0, len(preorder)-1)