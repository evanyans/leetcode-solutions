class Solution:
    # Attempted 3/27/2025
    # AHA: learned about binary search on solution spaces
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # check if task is possible on an item in the solution space
        def check(k):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / k)
            return hours <= h
        # let us binary search on the solution space
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
