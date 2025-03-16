class Solution:
    # Attempted3/15/2025
    # AHA: now i understand DP 1d
    def rob(self, nums: List[int]) -> int:

        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            # Either rob first house (means we must rob thid house)
            #   or we rob 2nd house (means we dindt rob first house)
            memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))
            return memo[i]
        return dp(0)
