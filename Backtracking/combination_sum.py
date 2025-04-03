class Solution:
    # Attempted 4/3/2025
    # AHA: we can reuse numbers, i.e. keep start at same index.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, total, start):
            if total == target:
                ans.append(curr[:])
                return
            for i in range(start, len(candidates)):
                if total + candidates[i] <= target:
                    curr.append(candidates[i])
                    backtrack(curr, total + candidates[i], i)
                    curr.pop()
        ans = []
        backtrack([], 0, 0)
        return ans
