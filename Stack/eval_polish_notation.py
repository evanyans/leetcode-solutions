class Solution:
    # Attempted 4/25/2025
    # AHA: just like dr racket operations, process as you go
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }
        # once you get an operation, start popping
        for token in tokens:
            if token in operations:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                res = operations[token](num1, num2)
                stack.append(res)
            else:
                stack.append(token)
        return int(stack[0])


