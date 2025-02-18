class Solution:
    # Atempted 2/18/2025
    # AHA: remember there are two o's and two l's
    def maxNumberOfBalloons(self, text: str) -> int:
        hm = {
            'b' : 0,
            'a' : 0,
            'l' : 0,
            'o' : 0,
            'n' : 0
        }
        for c in text:
            if c in hm:
                if c == "o" or c == "l":    
                    hm[c] += 0.5
                else:
                    hm[c] += 1
        # minimum's max is 10^4 / 7 (7 letters in balloon)
        min_num = 1428
        for key in hm:
            if hm[key] < min_num:
                min_num = hm[key]
        return floor(min_num)
                
            
