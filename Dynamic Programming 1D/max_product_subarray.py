class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadanes Algorithm (yes i googled it, how would you come up with that bro)
        finalMax = nums[0]
        curMin = 1
        curMax = 1
        for n in nums:
            # attempt to calculate max
            temp = curMax * n
            # maximum of attempt, check if minimum can be converted to a bigger number,
            # and just the number itself
            curMax = max(temp, n * curMin, n)
            # update our curMin the same way to have the potential to grow to a max
            curMin = min(temp, n * curMin, n)
            
            # update our result
            finalMax = max(finalMax, curMax)
        return finalMax

