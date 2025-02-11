class Solution:
    # Attempted 2/10/2025
    # AHA: make sure to iterate backwards from the squares negatives.
    def sortedSquares(self, nums: List[int]) -> List[int]:
        m = 0
        collect_neg = []
        #all the positive numbers stay in place,
        # square -> reverse negative numbers, save that as an array
        for i, n in enumerate(nums):
            if n < 0:
                print(n ** 2)
                collect_neg.append(n ** 2)
                m += 1
            else:
                nums[i] = n ** 2
                
            
            
        l = len(collect_neg) - 1
        res = []
        # iterate through all the positive numbers
        while l >= 0 and m < len(nums):
            if collect_neg[l] < nums[m]:
                res.append(collect_neg[l])
                l -= 1
            elif collect_neg[l] >= nums[m]:
                res.append(nums[m])
                m += 1
                
        while l >= 0:
            res.append(collect_neg[l])
            l -= 1

        while m < len(nums):
            res.append(nums[m])
            m += 1

        
        return res
            
        
        
        
            
            
