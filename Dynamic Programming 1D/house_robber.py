class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def rob_solve(idx):
            if idx >= len(nums):
                return 0
            if idx in memo:
                return memo[idx]

            # rob first house, then we can only rob the 3rd house now
            rob_first = nums[idx] + rob_solve(idx + 2)
            # dont rob first house, then we can only rob the 2nd house 
            rob_second = rob_solve(idx + 1)

            memo[idx] = max(rob_first, rob_second)
            return memo[idx]
        return rob_solve(0)
        