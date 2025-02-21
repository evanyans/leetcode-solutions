class Solution:
    # Attempted 2/21/2025
    # AHA: very easy stack popping
    def makeGood(self, s: str) -> str:
        # first criteria just means i within range
        stack = []
        for c in s:
            if stack and c != c.lower() and stack[-1] == c.lower():
                stack.pop()
                continue
            if stack and c != c.upper() and stack[-1] == c.upper():
                stack.pop()
                continue
            stack.append(c)
        return "".join(stack)
