# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 2/27/2025
    # AHA: Get the append order correct, left first or right first.
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        if not root:
            return []
        # since we start with left to right
        # lets say left is false, right is true
        
        switch = True
        ans = []
        while queue:
            #logic for current level
            switch = not switch
            level_ans = []
            queue_len = len(queue)
            for _ in range(queue_len):
                if not switch:
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    # since we pop from the right now,
                    # we want to append the right node first so that
                    # when we alternate again, the order is correct.
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                    
                level_ans.append(node.val)
            ans.append(level_ans)
                        
        return ans
                
