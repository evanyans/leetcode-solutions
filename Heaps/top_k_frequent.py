class Solution:
    # reattempted 4/9/2025
    # AHA: basic heap template
    class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        nums_count = Counter(nums)
        for key, val in nums_count.items():
            # heap is minheap by default, i.e. we will pop smallest
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]
    # Attempted 3/29/2025
    # AHA: when we do a minheap, we pop smallest elements, reemember htat
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [] # heap is min by default
        freq_nums = Counter(nums)
        for key, val in freq_nums.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num[1] for num in heap]


