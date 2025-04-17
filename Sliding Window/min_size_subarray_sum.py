class Solution:
    # Attempted 4/17/2025
    # AHA; biggest mistake, window condition, and updating answer should occur before window moves
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = curr_window = 0
        ans = float('inf')
        for right in range(len(nums)):
            curr_window += nums[right]
            # window condition broken is if subarray less than target
            while curr_window >= target:
                ans = min(ans, right - left + 1)
                curr_window -= nums[left]
                left += 1
            #ans = min(ans, right - left + 1)
        return ans if ans != float('inf') else 0

