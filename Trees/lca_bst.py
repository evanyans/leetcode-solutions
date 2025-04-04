# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Attempted 3/16/2025
    # AHA: use existence as a boolean
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return None
            if root == p or root == q:
               return root

            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                return root
            elif left:
                return left
            return right
        return dfs(root)
