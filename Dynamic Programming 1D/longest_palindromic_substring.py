class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = ""
        palLen = 0
        str_len = len(s)
        for i in range(str_len):
            l = i
            r = i
            while l >= 0 and r < str_len and s[l] == s[r]:
                if (r - l + 1) > palLen:
                    pal = s[l : r + 1]
                    palLen = r - l + 1
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < str_len and s[l] == s[r]:
                if (r - l + 1) > palLen:
                    pal = s[l : r + 1]
                    palLen = r - l + 1
                l -= 1
                r += 1
        return pal


