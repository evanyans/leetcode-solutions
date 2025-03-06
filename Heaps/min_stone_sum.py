class Solution:
    # Attempted 3/6/2025
    # AHA: how is this medium, just use heap. remember time complexities
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Since we want minimum, we will always want to take
        # the maximum and divide it by 2, so lets use a heap
        for i in range(len(piles)):
            piles[i] = -piles[i]
        heapq.heapify(piles)
        while k > 0:
            x = heapq.heappop(piles)
            x = floor(x / 2)
            heapq.heappush(piles, x)
            k -= 1
        
        total = 0
        for n in piles:
            total += -n
        return total
