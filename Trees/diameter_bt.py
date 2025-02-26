# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 2/25/2025
    # AHA: you need to use nonlocal or list since integers are immutable inside functions
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len = [0]
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            max_len[0] = max(max_len[0], l + r)
            return max(l, r) + 1
        
        dfs(root)
        return max_len[0]
