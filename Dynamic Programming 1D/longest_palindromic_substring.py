class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = ""
        # Returns the longest string length a given character
        def expand(p1, p2) -> str:
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                p1 -= 1
                p2 += 1
            #add one to the left because we have reached -1,
            #keep p2 the same because we have reached past the length
            return s[p1+1:p2]

        for i in range(len(s)):
            pali = expand(i, i)
            if len(pali) > len(longest):
                longest = pali
            pali = expand(i, i+1)
            if len(pali) > len(longest):
                longest = pali

        return longest

    
        



        
