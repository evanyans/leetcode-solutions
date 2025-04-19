# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  # Attempted /419/2025
  # AHA: basic BFS
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Basic BFS, calcualate averages for each
        queue = deque([root])
        ans = []
        while queue:
            cur_len = len(queue)
            cur_sum = 0
            for _ in range(cur_len):
                node = queue.popleft()
                cur_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(cur_sum / cur_len)
        return ans
            
    
