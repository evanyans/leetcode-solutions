class Solution:
    # Attempted 2/11/2025
    # AHA: its just implement prefix sum
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            
        return prefix
