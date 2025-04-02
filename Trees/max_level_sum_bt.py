# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 4/1/2025
    # AHA: remember to correctly initalize variables, template bfs
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        max_sum = root.val
        level = 1
        ans = level
        while queue:
            queue_len = len(queue)
            level_sum = 0
            for i in range(queue_len):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                ans = level
            level += 1
        return ans

