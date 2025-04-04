# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Attempted 4/4/2025
    # AHA: postorder traversal.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return None
            if root == p or root == q:
                return root

            # search left tree and right tree
            left = dfs(root.left)
            right = dfs(root.right)
            # both left and right contain p and q, i.e. we must return root
            if left and right:
                return root
            elif left: #only left contains both
                return left
            else: # only right contains both
                return right
        
        return dfs(root)
            
