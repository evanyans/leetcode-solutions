# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 4/26/2025
    # AHA: basic bfs template
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        #bfs to the last row, pick the leftmost element
        queue = deque([root])
        ans = []
        while queue:
            cur_arr = []
            cur_len = len(queue)
            for _ in range(cur_len):
                node = queue.popleft()
                cur_arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(cur_arr)
        return ans[-1][0]
            
