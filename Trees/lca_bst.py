# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Re-Attempted 4/4/2025 
    # AHA: OHH WE ARE LOOKING FOR THE SPLIT POINT USING BINARY SEARCH
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # lets just make p the smaller one
        if p.val > q.val:
            tmp = q
            q = p
            p = tmp
        while root:
            if q.val < root.val: #both values are in the left tree
                root = root.left
            elif p.val > root.val: #both values are in the right tree
                root = root.right
            else:
                return root
            
