class Solution:
    # Attempted 3/8/2025
    # AHA: 
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        def backtrack(curr, node):
            if node == target:
                ans.append(curr[:])
                return
            for neighbor in graph[node]:
                curr.append(neighbor)
                backtrack(curr, neighbor)
                curr.pop()

        ans = []
        backtrack([0], 0)
        return ans
