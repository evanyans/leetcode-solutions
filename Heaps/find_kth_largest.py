class Solution:
    # Attempted 3/6/2025
    # AHA: has to be an easy, why medium.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        ans = 0
        while k > 0:
            ans = heapq.heappop(nums)
            k -= 1
        return -ans
