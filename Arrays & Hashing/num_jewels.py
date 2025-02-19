class Solution:
    # Attempted 2/19/2025
    # Aha: this is like braindead
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_dict = set(jewels)
        count = 0
        for c in stones:
            if c in jewel_dict:
                count += 1
        return count
        
