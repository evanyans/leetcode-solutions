class Solution:
    # Attempted 2/18/2025
    # aha: Subarray means sliding window. Mapped this problem onto a "subarray sum = k" question
    def findMaxLength(self, nums: List[int]) -> int:
        #sliding window problem because it asks for max subarray
        
        # preprocess so that 0's are -1's to have a cancel out property.
        # Since we preprocessed, we can rephrase problem as: find max len of subarray
        # where the sum is equal to 0.
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
                
        # curr is our current prefix sum
        # indicies holds first index of 
        curr = max_len = 0
        indicies = defaultdict(int)
        indicies[0] = -1
        for i, n in enumerate(nums):
            curr += n
            if curr - 0 in indicies:
                cur_len = i - indicies[curr - 0]
                max_len = max(max_len, cur_len)
            if curr - 0 not in indicies:
                indicies[curr] = i

        return max_len
            
                
            
