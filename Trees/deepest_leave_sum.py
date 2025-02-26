# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 2/26/2025
    # AHA: mixing dfs and bfs.
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        #dfs to find maxdepth
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            return max(l, r) + 1
        depth = dfs(root) 
        print(depth)
    
        queue = deque([root])
        ans = 0
        count_depth = 0
        while queue:
            count_depth += 1
            num_in_level = len(queue)
            for _ in range(num_in_level):
                
                node = queue.popleft()
                if count_depth == depth:
                    ans += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
        
