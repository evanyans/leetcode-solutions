# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Attempted 3/19/2025
    # AHA: use the BST property
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal causes sorted traversal:
        arr = []
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        return arr[k - 1]


        # BRUTE FORCE O(N LOG K) SOLUTION, only makes sense for BT
        # does not make sense for BST

        # heap = []
        # def dfs(root):
        #     if not root:
        #         return
        #     heapq.heappush(heap, -root.val)
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # return -heap[0]
