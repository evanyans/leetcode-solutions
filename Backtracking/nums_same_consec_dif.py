class Solution:
    # Attempted 3/10/2025
    # AHA: we are kickstarting what the "last" element is through the for loop
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(curr, last):
            if len(curr) == n:
                if curr[0] == '0':
                    return
                ans.append(int("".join(curr)))
                return
            for i in range(10):
                if abs(i - last) == k:
                    curr.append(str(i))
                    backtrack(curr, i)
                    curr.pop()
            
        ans = []
        for i in range(10):
            backtrack([str(i)], i)
        return ans
