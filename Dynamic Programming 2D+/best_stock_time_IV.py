class Solution:
    # Attempted 3/12/2025
    # AHA: just evaluate all choices and attempt all of them recursively
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = {}
        def dp(i, holding, remain):
            if i >= len(prices) or remain == 0:
                return 0
            if (i, holding, remain) in memo:
                return memo[(i, holding, remain)]
            ans = dp(i + 1, holding, remain)
            if holding: # compare/max of skipping vs. selling
                ans = max(ans, prices[i] + dp(i + 1, False, remain - 1))
            else: # compare/max of skipping vs buying
                ans = max(ans, -prices[i] + dp(i + 1, True, remain))
            memo[(i, holding, remain)] = ans
            return memo[(i, holding, remain)]
        return dp(0, False, k)
