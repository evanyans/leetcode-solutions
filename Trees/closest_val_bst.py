# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 2/27/2025
    # AHA: dumb edge case, iterate using bst but find min dif
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = 0
        min_dif = 10**9
        def solve(root):
            nonlocal closest
            nonlocal min_dif
            if not root:
                return
            if abs(target - root.val) < min_dif:
                min_dif = abs(target - root.val)
                closest = root.val
            # stupid edge case where we must round down on .5
            elif abs(target - root.val) == min_dif:  
                closest = min(closest, root.val) 
                
            if target < root.val:
                solve(root.left)
            elif target > root.val:
                solve(root.right)
        solve(root)
        return closest
