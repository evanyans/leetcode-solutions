class Solution:
    # Attempted 3/14/2025
    # AHA: typical backtracking, understand why we do i+1 as our start
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(curr, start):
            if len(curr) == k:
                ans.append(curr[:])
                return
            for i in range(start, n + 1):
                curr.append(i)
                backtrack(curr, i + 1)
                curr.pop()
        backtrack([], 1)
        return ans
