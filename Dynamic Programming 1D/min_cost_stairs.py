class Solution:
    # Attempted 3/11/2025
    # AHA: reccurence relation is the hardest part
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # these base cases work becase getting to step 0 or step 1 costs nothing
        memo = {0:0, 1:0}
        #returns cost
        def dp(i):
            if i in memo:
                return memo[i]
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]
        return dp(len(cost))
