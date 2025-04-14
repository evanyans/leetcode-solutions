class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        # 73 [73]
        # 76 (73 < 76) pop 73 [73] -> [] -> [76]
        # 72 (76 > 72) [76, 72]
        # 69 (72 > 69) [76, 72, 69]
        # 71 (69 < 71) pop 69 [76, 72, 69] -> [76, 72] -> [76, 72, 71]
        for i in range(len(temperatures) - 1, -1, -1):
            # Pop indices of days with temperatures less than or equal to today
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i

            stack.append(i)
        print(stack)
        print(ans)
        return ans




