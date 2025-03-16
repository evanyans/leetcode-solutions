class Solution:
    # Attempted 3/15/2025
    # AHA: its just mapping to houserobber 1 but noticing the difference here.
    def rob(self, nums: List[int]) -> int:
        
        def rob_one(nums):
            memo = {}
            def dp(i):
                if i >= len(nums):
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))
                return memo[i]
            return dp(0)

        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            # Robbing the first means we cant rob the last
            # We either rob first house to n-1
            # or rob 2nd house to n
            
            memo[i] = max(rob_one(nums[:-1]), rob_one(nums[1:]))
            return memo[i]
        if len(nums) == 1:
            return nums[0]
        return dp(0)
            
