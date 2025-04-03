class Solution:
    # Attmepted 4/3/2025
    # AHA: bunch of dumb edge cases
    def myAtoi(self, s: str) -> int:

        # Case 1: ignore leading whitespace
        idx = 0
        while  idx < len(s) and s[idx] == ' ':
            idx += 1

        # Case 2: check signs
        positive = True
        if idx < len(s) and (s[idx] == '-' or s[idx] == '+'):
            if s[idx] == '-':
                positive = False
            idx += 1

        # Case 3: skip leading 0's, form answer
        while idx < len(s) and s[idx] == '0':
            idx += 1

        ans = 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        for i in range(idx, len(s)):
            if ord(s[i]) > 57 or ord(s[i]) < 48:
                break
            curr_num = (ord(s[i]) - ord('0'))
            if ans > INT_MAX // 10 or (ans == INT_MAX // 10 and curr_num > INT_MAX % 10):
                return INT_MAX if positive else INT_MIN
            if ans < INT_MIN // 10 or (ans == INT_MIN // 10 and -curr_num < INT_MIN % 10):
                return INT_MIN if positive else INT_MAX
            ans = ans * 10 + curr_num

        if not positive:
            ans = -ans

 
        return ans
            
