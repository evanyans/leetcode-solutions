class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        ans = 0
        nums.sort()
        # [1, 3, 3, 3, 4]
        while left < right:
            if nums[left] + nums[right] > k: # too big, bring down right
                right -= 1
            elif nums[left] + nums[right] < k: # too small, bring up left
                left += 1
            else: # == k
                ans += 1
                left += 1
                right -= 1
        return ans
