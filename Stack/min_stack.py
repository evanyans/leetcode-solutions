# Attempted 4/24/2025
# AHA: internal stack keeps minimum of current state
class MinStack:
    # [1, 4, 6, 8]
    def __init__(self):
        self.external_stack = []
        self.internal_stack = []

    def push(self, val: int) -> None:
        self.external_stack.append(val)
        if self.internal_stack:
            self.internal_stack.append(min(val, self.internal_stack[-1]))
        else:
            self.internal_stack.append(val)

        

    def pop(self) -> None:
        self.external_stack.pop() # assumption in question
        self.internal_stack.pop()



    def top(self) -> int:
        return self.external_stack[-1]  # assumption in question


        
    def getMin(self) -> int:
        return self.internal_stack[-1]  # assumption in question
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
