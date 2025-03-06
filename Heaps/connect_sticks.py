class Solution:
    # Attempted 3/6/2025
    # AHA: also easy heap question, greedyish too. remember time complexities
    def connectSticks(self, sticks: List[int]) -> int:
        # Since x + y punishes us for higher sums
        # let's only connect the smallest two sticks
        # which should give us the smallest numbers
        heapq.heapify(sticks)
        n = len(sticks)
        cost = 0
        while n > 0:
            x = heapq.heappop(sticks)
            n -= 1
            if n <= 0:
                return cost
            y = heapq.heappop(sticks)
            #n -= 1
            cost += (x + y)
            heapq.heappush(sticks, x + y)
            #n += 1
        return cost
