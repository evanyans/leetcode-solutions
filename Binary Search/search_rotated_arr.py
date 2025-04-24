class Solution:
    # Attempted 4/23/2025
    # AHA: if statement logical
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if left == right:
            return 0 if nums[left] == target else -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]: #implies left -> mid is ascending
                if nums[left] <= target <= nums[mid]: # if number is between left -> mid, bs it
                    right = mid - 1
                else: # target is in mid < target < right
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


