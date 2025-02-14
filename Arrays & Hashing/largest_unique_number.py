class Solution:
    # Attempted 2/13/2025
    # aha: preprocess is cool, understand when to use key and value
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # preprocess to count occurences
        hm = defaultdict(int)
        for i in range(len(nums)):
            hm[nums[i]] += 1
            
        max_num = -1
        for key in hm:
            if hm[key] > 1:
                continue
            if key > max_num:
                max_num = key
            

        return max_num
