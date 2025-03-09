class Solution:
    # Attempted 3/8/2025
    # AHA: please learn backtracking better
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans
