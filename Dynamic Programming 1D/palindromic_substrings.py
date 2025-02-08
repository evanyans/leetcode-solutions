class Solution:
    # Attempted 2/8/2025
    # Aha: this is just longest palindromic substring but without the longest
    def countSubstrings(self, s: str) -> int:
        # use the outwards technique again

        # returns the largest palindrome
        def expand(p1, p2):
            palindromes = 0
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                palindromes += 1
                p1 -= 1
                p2 += 1
            return palindromes

        curSum = 0
        for i in range(len(s)):
            sub1 = expand(i, i)
            sub2 = expand(i, i+1)
            curSum += sub1
            curSum += sub2

        return curSum

            
            
