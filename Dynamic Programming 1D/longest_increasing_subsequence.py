class Solution:
    # Attempted 3/11/2025
    # AHA: identify output -> identify recurrence relation & variables -> implement

    # [10, 9, 2, 5, 3, 7, 101, 18]
    # how do we know to take 10? if the previous numbers are less than 10.
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        #returns the longest increasing subsequence based on an index
        def solve(i):
            if i in memo:
                return memo[i]
            ans = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    ans = max(ans, solve(j) + 1)

            memo[i] = ans
            return ans

        max_sol = 0
        # iterate through all indicies for possible subsequences
        for i in range(len(nums)):
            max_sol = max(max_sol, solve(i))
        return max_sol
