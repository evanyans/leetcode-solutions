# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 3/24/2025
    # AHA: make sure base case is correct
    # if both dont exist, its same, if one doesnt and other
    # does, then its wrong
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        return dfs(p, q)
        
