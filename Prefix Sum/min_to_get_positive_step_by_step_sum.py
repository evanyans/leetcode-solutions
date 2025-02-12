class Solution:
    # Attempted 2/11/2025
    # AHA Moment:
    #       - neat trick with finding minimum of prefix sum
    #       - if minimum is positive, then it ruins the purpose of the algorithm, so just return 1.
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        minimum = nums[0]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            if prefix[i] < minimum:
                minimum = prefix[i]
        if minimum <= 0:
            return minimum * (-1) + 1
        return 1
             
        # [-3, 2, -3, 4, 2] original array
        # [-3, -1, -4, 0, 2] prefix sum
        # [1, 3, 0, 4, 6]
            
        
