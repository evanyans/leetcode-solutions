class Solution:
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


