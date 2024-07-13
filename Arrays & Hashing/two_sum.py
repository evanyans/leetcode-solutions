class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for i, n in enumerate(nums):
            if target - n in hasher:
                return [hasher[target - n], i]
            hasher[n] = i
