class Solution:
    # Attempted 3/6/2025
    # AHA: remember when to use maxheap, when to use minheap
    # here we needed to keep smallest elements, so we pop the largest, so maxheap
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #lets store a heap of distances
        # Since we want close points we need small distances, we want to pop max's, so use maxheap
        heap = []
        for x, y in points:
            heapq.heappush(heap, (-sqrt(x**2 + y**2), (x, y)))
            if len(heap) > k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]
