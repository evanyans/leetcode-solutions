# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 2/23/2025
    # aha: if left doesnt exist, we dont want to count it
    # or else it will end up being depth 1, and min(1, ..) will jst be 1
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        return min(l, r) + 1
        
        
