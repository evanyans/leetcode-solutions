class Solution:
    # Attempted 3/27/2025
    # AHA: its just binary search template, logically think about it.
    def findMin(self, nums: List[int]) -> int:
        # BINARY SEARCH SOLUTION O(LOGN):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
            

        # BRUTE FORCE SOLUTION O(N):
        # Since sorted ascending, we will hit a point where next is less than current
        #   if we dont hit that point, we have a sorted normal array
        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i + 1]:
        #         return nums[i + 1]
        #         break
        # return nums[0]
    
