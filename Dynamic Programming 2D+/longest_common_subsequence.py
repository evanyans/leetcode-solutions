class Solution:
    # Attempted 3/12/2025
    # AHA: forgot to add the counter for length.
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # returns the length of the longest common subsequence
        # when we start at ith character of text1 and jth character of text2
        memo = { }
        def dp(i, j):
            # either text1[i] == text2[j]
                # increase length, both i and j must progress by 1
            # or     text1[i] != text2[j]
                # need to decide,  move i or move j, well lets just try both cases with dp
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                memo[(i, j)] = dp(i + 1, j + 1) + 1
                return memo[(i, j)]
            memo[(i, j)] = max(dp(i + 1, j), dp(i, j + 1))
            return memo[(i, j)]
        return dp(0, 0)
