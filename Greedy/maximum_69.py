class Solution:
    # Attempt 3/6/2025
    # AHA: greedy simple
    def maximum69Number (self, num: int) -> int:
        #prio earliest 6
        num = str(num)
        ans = ['0'] * len(num)
        finished = False
        for i, n in enumerate(num):
            if not finished and n == "6":
                ans[i] = "9"
                finished = True
                continue
            ans[i] = n
        
        return int("".join(ans))
