# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, max_val, min_val):
            if not root:
                return max_val - min_val
            max_val = max(root.val, max_val)
            min_val = min(root.val, min_val)
            
            l = dfs(root.left, max_val, min_val)
            r = dfs(root.right, max_val, min_val)
            
            return max(l, r)
        
        
        return dfs(root, root.val, root.val)
        
        
        
            
        
        
        
        
