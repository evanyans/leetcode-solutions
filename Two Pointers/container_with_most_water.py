class Solution:
    # ReAttempted 4/5/2025
    # AHA: write out a test case, think about how to progress l and r
    def maxArea(self, height: List[int]) -> int:
        # observations: we start on outside for max width
        l = 0
        r = len(height) - 1
        max_water = 0
        while l < r:
            # 1, 8, 6, 2, 5, 4, 8, 3, 7
            # 0, 1, 2, 3, 4, 5, 6, 7, 8
            # 8 - 1 = 7 * 7 = 49
            water = min(height[l], height[r]) * (r - l)
            max_water = max(max_water, water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water

        


            
