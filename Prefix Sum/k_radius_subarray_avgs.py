class Solution:
    # Attempted 2/11/2025
    # AHA moment: just prefix sum it, make sure you know which boundaries to get subarray sums
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            # nums = [7,4,3,9,1,8,5,2,6], k = 3
            #  [-1,-1,-1,5,4,4,-1,-1,-1]
            # prefix = [7, !!11, 14, 23, 24, 32, 37, !!39, 45], k = 3
            # (39 - 11) // 7
            # 
        for i in range(len(nums)):
            # out of bounds means just ma ke it -1
            if i - k < 0 or i + k >= len(nums):
                nums[i] = -1
                continue
            if i - k - 1 < 0:
                nums[i] = prefix[i + k] // (k + k + 1)
                continue
            nums[i] = (prefix[i + k] - prefix[i - k - 1]) // (k + k + 1)
        return nums
