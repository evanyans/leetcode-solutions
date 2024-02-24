class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Example 1:
        # nums = [1, 2, 3, 4]
        # [2*3*4, 1*3*4, 1*2*4, 1*2*3]

        # O(n) time solution

        soln = [1] * len(nums)
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i, num in enumerate(nums):
            if i == 0:
                prefix[i] = num
            else:
                prefix[i] = num * prefix[i-1]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = nums[i]
            else: 
                suffix[i] = nums[i] * suffix[i+1] 

        # [1, 2, 6, 24]
        # [24, 24, 12, 4]

        for i in range(len(nums)):
            if i == 0:
                soln[i] = suffix[i+1]
            elif i == len(nums) - 1:
                soln[i] = prefix[i-1]
            else:
                soln[i] = prefix[i-1] * suffix[i+1]

        return soln





