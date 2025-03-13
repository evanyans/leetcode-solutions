class Solution:
    # Solved 3/13/2025
    # AHA: read the question properly, fee is only charged once, my mistake was that
    # i charged the fee twice.
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dp(i, holding):
            if i >= len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            ans = dp(i + 1, holding)
            if holding: #compare skipping with selling
                ans = max(ans, (prices[i] - fee) + dp(i + 1, False))
            else: #compare skiping with buying
                ans = max(ans, (-prices[i]) + dp(i + 1, True))
            memo[(i, holding)] = ans
            return memo[(i, holding)]

        return dp(0, False)
