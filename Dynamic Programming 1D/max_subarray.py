class Solution:
  # Attempted 2/7/2025
  # aha: remember to set maxSum to the starting element.
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane algorthm again?
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            curSum = max(curSum, 0)
            curSum = n + curSum
            maxSum = max(maxSum, curSum)

        return maxSum
