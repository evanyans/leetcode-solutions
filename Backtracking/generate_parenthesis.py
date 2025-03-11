class Solution:
    # Attempted 3/10/2025
    # AHA: we dont need the for loop here.
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, openers, closers):
            if len(curr) == n * 2:
                ans.append("".join(curr))
                return
            if openers < n:
                curr.append('(')
                backtrack(curr, openers + 1, closers)
                curr.pop()
            if closers < openers:
                curr.append(')')
                backtrack(curr, openers, closers + 1)
                curr.pop()
            
        ans = []
        backtrack([], 0, 0)
        return ans

    
            
