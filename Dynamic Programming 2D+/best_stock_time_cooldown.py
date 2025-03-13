class Solution:
    # Attempted 3/13/2025
    # AHA: i used a third parameter, "cooldown", but I needed to just
    # implicitly set a cooldown by just progressing an extra day to save
    # alot of memory.
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, holding):
            if i >= len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            ans = dp(i + 1, holding)
            if holding: # compare skipping with selling
                ans = max(ans, prices[i] + dp(i + 2, False))
            else:
                ans = max(ans, -prices[i] + dp(i + 1, True))

            memo[(i, holding)] = ans
            return memo[(i, holding)]
        return dp(0, False)


