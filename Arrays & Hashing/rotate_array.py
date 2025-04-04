class Solution:
    # Attempted 4/3/2025
    # AHA: remember wrap around using modulus
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l < r:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
                l += 1
                r -= 1
        n = len(nums)
        k = k % n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        
        

        
