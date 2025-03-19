# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 3/18/2025
    # AHA: its just bfs, make sure ur appending the value and not the node to the answer
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # isnt this just implement bfs
        if not root:
            return []

        queue = deque([root])
        ans = []
        while queue:
            level = []
            curr_len = len(queue)
            for _ in range(curr_len):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        return ans
