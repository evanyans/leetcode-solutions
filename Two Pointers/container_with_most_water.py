class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        max_area = 0
        temp_area = 0

        while p1 < p2:
            width = p2 - p1

            temp_area = min(heights[p1], heights[p2]) * width
            
            if temp_area > max_area:
                max_area = temp_area

            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1

        return max_area