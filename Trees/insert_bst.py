# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 2/27/2025
    # AHA: remember the empty edge case
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # edge case for empty root
        if not root:
            root = TreeNode(val)
            return root
        
        def solve(root, parent):
            if not root and val < parent.val:
                parent.left = TreeNode(val)
                return
            elif not root and val > parent.val:
                parent.right = TreeNode(val)
                return
            # equals case does not exist according to restrictions
            if val < root.val:
                solve(root.left, root)
            elif val > root.val:
                solve(root.right, root)
        solve(root, root)
        return root
