class Solution:
    def isValid(self, s: str) -> bool:
        dicty = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for c in s:
            if c in dicty and stack:
                if stack.pop() != dicty[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0            
