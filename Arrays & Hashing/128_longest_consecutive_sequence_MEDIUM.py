class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # cannot sort
        if not nums:
            return 0

        num_set = set(nums)
        largest = 0

        for num in nums:
            if num - 1 not in num_set:
                current = 1
                temp_num = num + 1
                while temp_num in num_set:
                    current += 1
                    temp_num += 1
                largest = max(largest, current)

        return largest
        