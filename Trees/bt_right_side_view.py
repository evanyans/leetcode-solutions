# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 3/18/2025
    # its just bfs but get the last element, easypz
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            curr_len = len(queue)
            for i in range(curr_len):
                # if we reached last element, append to ans
                node = queue.popleft()
                if i == curr_len - 1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans

