class Solution:
    # Attempted 2/12/2025
    # AHA: rememeber to add 1 to the length because [0,1] means length of 2       so we iterate 0, 1, 2
    def missingNumber(self, nums: List[int]) -> int:
        my_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in my_set:
                return i
        return -1
