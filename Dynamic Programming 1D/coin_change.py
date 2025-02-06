# Attempted 2/5/2025 for the first time
# Aha moment: Bottom-up dynamic programming (focus on the smallest case of calculating coinChange for amount 0)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Speaking in example 1
        # Initialize array with amount 0-11, which is why we do +1
        dp = [amount + 1] * (amount + 1) 

        # lets do bottom-up dp where we imagine how many coins it takes to form amount 0
        dp[0] = 0

        for i in range(1, amount + 1):
            for n in coins:
                # i - n represents the remainder coins needed to form the current "amount"
                if i - n >= 0:
                    # - minimum of itself (check see if we already have better/worse previous solution)
                    # - 1 + dp[i-c] represents us calculating dp of i.
                    dp[i] = min(dp[i], 1 + dp[i - n])

        if dp[amount] == amount + 1:
            return -1
        return dp[amount]


