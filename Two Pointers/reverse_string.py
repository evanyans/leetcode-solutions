class Solution:
  #attempted 2/10/2025
  # AHA: very simple
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        
        while l < r:
            tmp = s[r]
            s[r] = s[l]
            s[l] = tmp
            l += 1
            r -= 1
            
