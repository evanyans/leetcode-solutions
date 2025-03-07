class Solution:
    # Attempted 3/7/2025
    # AHA: nlogn, could use bucket sort to achieve O(n)
    def minSetSize(self, arr: List[int]) -> int:
        # Always choose most occurences to remove
        occur = Counter(arr)
        if len(occur) == 1:
            return 1
        half_size = len(arr) // 2
        heap = []
        curr_occur = 0
        for key, val in occur.items():
            # iteratively add to the heap
            heapq.heappush(heap, -val)
            
        curr_occur = 0
        elements = 0
        while curr_occur < half_size:
            # take from the max heap to form our array
            curr_occur += -heapq.heappop(heap)
            # our "array" the actual heap is the leftovers
            elements += 1

        return elements
