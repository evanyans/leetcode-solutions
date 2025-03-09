class Solution:
    # Attempted 3/9/2025
    # aha: please redo, its not a nested for loop, please understand backtracking
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(curr, i):
            # base case
            if len(curr) == len(digits):
                ans.append("".join(curr[:]))
                return
            for c in mapping[digits[i]]:
                curr.append(c)
                backtrack(curr, i + 1)
                curr.pop()

        ans = []
        backtrack([], 0)
        return ans

  

            
