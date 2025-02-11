class Solution:
    # Attempted 2/11/2025
    # AHA: rememebr base case, also rememeber to update result on initial window
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        curr_avg = 0
        curr_sum = 0
        res = 0
        for i in range(k):
            curr_sum += nums[i]
            curr_avg = curr_sum / (i + 1)
            
        res = curr_avg
        for i in range(k, len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]
            curr_avg = curr_sum / k
            res = max(curr_avg, res)
            
        return res
            
