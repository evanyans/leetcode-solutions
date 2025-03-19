# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 3/18/2025
    # AHA: instead of thinking about tracking a path, think about what we really need to
    # keep track of, which is only the max element.
    def goodNodes(self, root: TreeNode) -> int:
        # lets dfs to make some paths
        # logic: in a path we only need to keep the max value
            # for comparison, if we are setting a new max value
            # for the path, we have found a good node
        if not root:
            return []
        ans = 0
        def dfs(root, curr_max):
            nonlocal ans
            if not root:
                return 
        
            if root.val >= curr_max:
                curr_max = root.val
                ans += 1

            dfs(root.left, curr_max)
            dfs(root.right, curr_max)

        dfs(root, root.val)
        return ans
