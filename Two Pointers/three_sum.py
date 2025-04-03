class Solution:
    # Attempted 4/3/2025
    # AHA: skip duplicates, we dont want duplicates
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #lock one number in, check for sum
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total == 0:
                    ans.append([nums[left], nums[right], nums[i]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
        return ans




        
