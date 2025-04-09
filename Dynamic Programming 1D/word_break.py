class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # does there exist some words in wordDict that can be used to
        # reconstruct string s?

        wordSet = set(wordDict)

        @lru_cache(None)
        def solve(idx) -> bool:
            # base case, if we hit the end of string, then it worked out
            if idx == len(s):
                return True
            # iterate from current idx to end of string
            # recursive progression until we finally hit the end
            for j in range(idx, len(s)):
                # brute force
                if s[idx: j + 1] in wordSet:
                    if solve(j + 1):
                        return True
            return False 

        return solve(0)




