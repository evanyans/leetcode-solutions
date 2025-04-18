class Solution:
    def trap(self, height: List[int]) -> int:
        left = water = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        while left < right:
            # move the smaller height inwards to trap water properly   
            # since left_max < right_max, right_max is taller, and left_max is the limiting wall for water
            if left_max < right_max:
                # move left inwards, update max left height
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        return water




            
