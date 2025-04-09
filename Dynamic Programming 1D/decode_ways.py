class Solution:
        # "1" -> 'A'
        # "2" -> 'B'
        # "..."
        # "25" -> 'Y'
        # "26" -> 'Z'
    # ATTEMPTED 4/8/2025
    # AHA: 
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # assume dp(i) returns number of ways to decode string
        # i is the starting index of the number
        #  dp(i) = dp(i + 1)
        #. dp(i) = 0
        #  dp(i) = dp(i + 1) + dp(i + 2)

        # Example 11106
        # 1, 1, 10, 6
        # 11, 10 6

        # dp(0) -> 
    
        # dp to find how many ways 11106 can be
        # segmented into numbers that fit 1 to 26

        memo = {}
        def dp(i) -> int:
            # base case is we finished the string, i.e. 1 valid way
            if i == len(s):
                return 1

            if i in memo:
                return memo[i]

            if s[i] == '0':
                return 0
            
            ans = dp(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i: i + 2]) <= 26:
                ans += dp(i + 2)

            memo[i] = ans
            return ans

        return dp(0)
        


            

            


        





            
