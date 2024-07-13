cache = {1: 1, 2: 2}
class Solution:
    # Without memoization, just pure recursion.
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    # With memoization, 
    def climbStairs(self, n: int) -> int:
        if n in cache:
            return cache[n]
        cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return cache[n]
