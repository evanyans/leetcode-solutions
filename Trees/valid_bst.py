# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 3/18/2025
    # AHA: make sure limits are set for each node, cant just check each node
    # individually
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        

        return dfs(root, float('-inf'), float('inf'))
