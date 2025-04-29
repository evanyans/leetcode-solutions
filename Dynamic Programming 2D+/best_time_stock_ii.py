class Solution:
    # Attempted 4/28/2025
    # AHA: dp format
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        # i: day
        # holding: bool
        def dp(i, holding):
            # base case
            if i >= len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]

            # recurrence relation
            ans = dp(i + 1, holding)
            if holding: #if holding, we try selling
                ans = max(ans, prices[i] + dp(i + 1, False))
            else: # if not holding, we try buying
                ans = max(ans, -prices[i] + dp(i + 1, True))
            memo[(i, holding)] = ans
            return memo[(i, holding)]
        return dp(0, False)

            
