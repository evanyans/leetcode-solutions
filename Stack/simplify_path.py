class Solution:
    # Attempted 2/20/2025
    # AHA moment: path.split("") and "/".join(stack) is quick work here.
    def simplifyPath(self, path: str) -> str:
        stack = []

        for comp in path.split("/"):
            print(comp)
            if comp == "" or comp == ".":
                continue
            elif stack and comp == "..":
                stack.pop()
                continue
            elif comp == "..": #edge case for when stack is empty (i.e we just have the root)
                continue
            stack.append(comp)
            
        # "/" + is used for the root directory
        return "/" + "/".join(stack)
