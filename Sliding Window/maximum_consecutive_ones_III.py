class Solution:
    # Attempted 2/11/2025
    # AHA moment: when in the inner while loop, make sure we keep iterating left side of window
    def longestOnes(self, nums: List[int], k: int) -> int:
        # With Max Consecutives ones if you can only flip 1 zero is just finding
        # longest subarray with at most 1 zero.
        
        # Since it is flip k zeros, we are now finding longest subarray with at most
        # k zeros because we can flip those k zeros to get the longest 1's
        
        left = curr = 0
        window_len = 0
        max_len = 0
        for right in range(len(nums)):
            # some logic to progress i
            if nums[right] == 0:
                curr += 1
            # progress the left side of the window until curr <= k
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            window_len = right - left + 1    
            max_len = max(window_len, max_len)
        return max_len
                
                
